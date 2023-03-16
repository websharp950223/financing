# -*- coding: utf-8 -*-
from odoo import api, fields, models


class GpaisRegistrationLineTransport(models.TransientModel):
    _name = 'gpais.registration.line.transport'

    klasifikacija = fields.Many2one('gpais.klasifikacija', string='Klasifikacija',
                                    domain="[('product_type', '=', 'transportoPriemone')]")
    activity_own_need = fields.Boolean(string='Sunaudojimas savo reikmėms')
    activity_b2c = fields.Boolean(string='Mažmeninė prekyba')
    activity_b2b = fields.Boolean(string='Didmeninė prekyba')
    activity_remote = fields.Boolean(string='Nuotolinė prekyba')
    activity_export_broker = fields.Boolean(string='Išvežimas iš LR vidaus rinkos per trečiuosius asmenis')

    @api.multi
    def get_line_values(self):
        res = [{
            'gpais_product_type': 'transportoPriemone',
            'klasifikacija': line.klasifikacija.id,
            'activity_own_need': line.activity_own_need,
            'activity_b2c': line.activity_b2c,
            'activity_b2b': line.activity_b2b,
            'activity_remote': line.activity_remote,
            'activity_export_broker': line.activity_export_broker,
        } for line in self]
        return res
