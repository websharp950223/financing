# -*- coding: utf-8 -*-
from odoo import models, fields, exceptions, api, _


class AmazonSPTaxRule(models.Model):
    _name = 'amazon.sp.tax.rule'
    _description = _('Model that holds configuration for tax application rules based on countries')

    @api.model
    def _default_taxes(self):
        """Get default taxes for products/services of the marketplace"""
        return self.env['account.tax'].search([
            ('code', '=', 'Ne PVM'), ('price_include', '=', True)], limit=1)

    name = fields.Char(string='Rule name', compute='_compute_name')
    rule_type = fields.Selection([
        ('country_to_country', 'Specific country to country shipping'),
        ('eu_to_eu', 'EU to EU shipping'),
        ('eu_to_other', 'EU to other country shipping'),
        ('other_to_other', 'Non-EU country shipping'),
        ('inter_shipping', 'Inter-country shipping'),
    ], string='Tax rule type', default='eu_to_other', inverse='_set_rule_type')

    marketplace_id = fields.Many2one(
        'amazon.sp.marketplace', string='Marketplace'
    )
    origin_country_id = fields.Many2one(
        'res.country', string='Origin country',
    )
    destination_country_id = fields.Many2one(
        'res.country', string='Destination country',
    )

    # Tax fields
    product_non_zero_rate_tax_id = fields.Many2one(
        'account.tax', string='Taxes for products (Non-zero rate)', default=_default_taxes,
        domain="[('price_include', '=', True), ('type_tax_use', '=', 'sale')]",
        required=True
    )
    service_non_zero_rate_tax_id = fields.Many2one(
        'account.tax', string='Taxes for services (Non-zero rate)', default=_default_taxes,
        domain="[('price_include', '=', True), ('type_tax_use', '=', 'sale')]",
        required=True
    )

    product_zero_rate_tax_id = fields.Many2one(
        'account.tax', string='Taxes for products (Zero rate)', default=_default_taxes,
        domain="[('price_include', '=', True), ('type_tax_use', '=', 'sale')]",
        required=True
    )
    service_zero_rate_tax_id = fields.Many2one(
        'account.tax', string='Taxes for services (Zero rate)', default=_default_taxes,
        domain="[('price_include', '=', True), ('type_tax_use', '=', 'sale')]",
        required=True
    )

    # Computes / Inverses ---------------------------------------------------------------------------------------------

    @api.multi
    def _set_rule_type(self):
        """Reset countries if rule type is not country to country"""
        rules = self.filtered(lambda x: x.rule_type != 'country_to_country')
        rules.write({'origin_country_id': False, 'destination_country_id': False})

    @api.multi
    def _compute_name(self):
        """Composes a name for Amazon SP tax rule"""
        for rec in self:
            if rec.rule_type == 'country_to_country':
                rule_name = _('Taxes: [{}] -> [{}]').format(
                    rec.origin_country_id.code,  rec.destination_country_id.code
                )
            else:
                rule_name = _('Taxes: {}').format(dict(self._fields['rule_type'].selection).get(rec.rule_type))
            rec.name = rule_name

    # Constraints -----------------------------------------------------------------------------------------------------

    @api.multi
    @api.constrains('origin_country_id', 'destination_country_id', 'rule_type', 'marketplace_id')
    def _check_country_consistency(self):
        """Ensure that only one rule exists for origin/destination country combination"""
        for rec in self:
            base_domain = [('rule_type', '=', rec.rule_type)]
            if rec.marketplace_id:
                base_domain += [('marketplace_id', '=', rec.marketplace_id.id)]
            # Check country to country types
            if rec.rule_type == 'country_to_country':
                if self.search_count(
                        [('origin_country_id', '=', rec.origin_country_id.id),
                         ('destination_country_id', '=', rec.destination_country_id.id)] + base_domain
                ) > 1:
                    raise exceptions.ValidationError(
                        _('Tax rule with the same origin and destination country already exists')
                    )
            else:
                # Otherwise one rule per type can exist
                if self.search_count(base_domain) > 1:
                    raise exceptions.ValidationError(_('Tax rule with the same configuration already exists'))

    # Main methods ----------------------------------------------------------------------------------------------------

    @api.model
    def get_tax_rule(self, destination_country, origin_country, marketplace):
        """
        Method that returns account tax record in found rule based on the passed settings
        :param destination_country: Shipping country to (record)
        :param origin_country: Shipping country from (record)
        :param marketplace: Amazon SP marketplace  (record)
        :return: Amazon tax rule (record)
        """

        tax_rule = None
        marketplace_domain = [('marketplace_id', '=', marketplace.id)]
        # 1st check -- Check global country group rules
        if destination_country == origin_country:
            rule_type = 'inter_shipping'
            tax_rule = self.search([('rule_type', '=', rule_type)] + marketplace_domain)
            if not tax_rule:
                tax_rule = self.search([('rule_type', '=', rule_type)])

        if not tax_rule:
            # Reference europe country group and determine rule type
            europe_group = self.env.ref('base.europe')
            # Check if destination and origin countries belong to EU
            dst_eu = destination_country in europe_group.country_ids
            org_eu = origin_country in europe_group.country_ids

            # Determine the rule type based on destination and origin countries
            rule_type = 'eu_to_other'
            if dst_eu and org_eu:
                rule_type = 'eu_to_eu'
            elif not dst_eu and not org_eu:
                rule_type = 'other_to_other'

            # Try to find the rule, include marketplace domain
            # otherwise, try to widen the domain by excluding the marketplace
            tax_rule = self.search([('rule_type', '=', rule_type)] + marketplace_domain)
            if not tax_rule:
                tax_rule = self.search([('rule_type', '=', rule_type)])

            # 2nd check -- Country to country (less common)
            if not tax_rule:
                c2c_domain = [
                    ('rule_type', '=', 'country_to_country'),
                    ('origin_country_id', '=', origin_country.id),
                    ('destination_country_id', '=', destination_country.id),
                ]
                tax_rule = self.search(c2c_domain + marketplace_domain)
                # If there's no rule, omit the marketplace
                if not tax_rule:
                    tax_rule = self.search(c2c_domain)
        return tax_rule
