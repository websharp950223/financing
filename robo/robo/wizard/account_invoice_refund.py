# -*- coding: utf-8 -*-
import logging
from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval
import traceback


_logger = logging.getLogger(__name__)


class AccountInvoiceRefund(models.TransientModel):
    _inherit = 'account.invoice.refund'

    def _get_user_refund_selection(self):
        selection_list = [('current_user', _('Me'))]
        if self.env.user.has_group(
                'robo.group_robo_invoice_crediting_associate_original_salesperson') or self.env.user.is_accountant():
            selection_list.append(('original_salesperson', _('Original salesperson')))
        return selection_list

    user_refund = fields.Selection(_get_user_refund_selection, string='Salesperson', default='current_user')

    @api.multi
    def invoice_refund_front(self):
        data_refund = self.read(['filter_refund'])[0]['filter_refund']
        return self.compute_refund_front(data_refund)

    @api.multi
    def compute_refund_front(self, mode='refund'):
        inv_obj = self.env['account.invoice']
        inv_tax_obj = self.env['account.invoice.tax']
        inv_line_obj = self.env['account.invoice.line']
        context = dict(self._context or {})
        xml_id = False

        for form in self:
            created_inv = []
            date = False
            description = False
            for inv in inv_obj.browse(context.get('active_ids')):
                if inv.state in ['draft', 'proforma2', 'cancel']:
                    raise UserError(_('Cannot refund draft/proforma/cancelled invoice.'))
                if inv.reconciled and mode in ('cancel', 'modify'):
                    raise UserError(_(
                        'Cannot refund invoice which is already reconciled, invoice should be unreconciled first. You can only refund this invoice.'))

                date = form.date or False
                description = form.description or inv.name
                user_id = self.env.user.id if self.user_refund == 'current_user' else \
                    self.env['account.invoice'].browse(self._context.get('active_id')).exists().user_id.id
                try:
                    refund = inv.with_context(user_id=user_id).refund(
                        form.date_invoice, date, description, inv.journal_id.id)
                except ValidationError as exc:
                    _logger.info(
                        '[{0}] User with id {1} failed to credit an invoice due to missing rights.'
                        '\nError: {2}]\nTraceback: {3}'.format(self.env.cr.dbname, self.env.user.id,
                                                               tools.ustr(exc), traceback.format_exc))
                    raise ValidationError(_('You do not have correct rights to credit invoices.'))
                refund.compute_taxes()

                created_inv.append(refund.id)
                if mode in ('cancel', 'modify'):
                    movelines = inv.move_id.line_ids
                    to_reconcile_ids = {}
                    to_reconcile_lines = self.env['account.move.line']
                    for line in movelines:
                        if line.account_id.id == inv.account_id.id:
                            to_reconcile_lines += line
                            to_reconcile_ids.setdefault(line.account_id.id, []).append(line.id)
                        if line.reconciled:
                            line.remove_move_reconcile()
                    refund.action_invoice_open()
                    for tmpline in refund.move_id.line_ids:
                        if tmpline.account_id.id == inv.account_id.id:
                            to_reconcile_lines += tmpline
                            to_reconcile_lines.filtered(lambda l: l.reconciled == False).reconcile()
                    if mode == 'modify':
                        invoice = inv.read(
                            ['name', 'type', 'number', 'reference',
                             'comment', 'date_due', 'partner_id',
                             'partner_insite', 'partner_contact',
                             'partner_ref', 'payment_term_id', 'account_id',
                             'currency_id', 'invoice_line_ids', 'tax_line_ids',
                             'journal_id', 'date'])
                        invoice = invoice[0]
                        del invoice['id']
                        invoice_lines = inv_line_obj.browse(invoice['invoice_line_ids'])
                        invoice_lines = inv_obj.with_context(mode='modify')._refund_cleanup_lines(invoice_lines)
                        tax_lines = inv_tax_obj.browse(invoice['tax_line_ids'])
                        tax_lines = inv_obj._refund_cleanup_lines(tax_lines)
                        invoice.update({
                            'type': inv.type,
                            'date_invoice': form.date_invoice,
                            'state': 'draft',
                            'number': False,
                            'invoice_line_ids': invoice_lines,
                            'tax_line_ids': tax_lines,
                            'date': date,
                            'origin': inv.origin,
                            'fiscal_position_id': inv.fiscal_position_id.id,
                        })
                        for field in ('partner_id', 'account_id', 'currency_id',
                                      'payment_term_id', 'journal_id'):
                            invoice[field] = invoice[field] and invoice[field][0]
                        inv_refund = inv_obj.create(invoice)
                        if inv_refund.payment_term_id.id:
                            inv_refund._onchange_payment_term_date_invoice()
                        created_inv.append(inv_refund.id)
                xml_id = (inv.type in ['out_refund', 'out_invoice']) and 'open_client_invoice' or \
                         (inv.type in ['in_refund', 'in_invoice']) and 'robo_expenses_action'
                # Put the reason in the chatter
                subject = _("Invoice refund")
                body = description
                refund.message_post(body=body, subject=subject)
        if xml_id:
            result = self.env.ref('robo.%s' % xml_id).read()[0]
            invoice_domain = safe_eval(result['domain'])
            invoice_domain.append(('id', 'in', created_inv))
            result['domain'] = invoice_domain
            return result
        return True
