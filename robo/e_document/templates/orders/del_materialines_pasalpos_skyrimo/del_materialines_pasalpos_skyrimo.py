# -*- coding: utf-8 -*-
from odoo import models, api


class EDocument(models.Model):
    _inherit = 'e.document'

    @api.multi
    def isakymas_del_materialines_pasalpos_skyrimo_workflow(self):
        self.ensure_one()
        # No workflow


EDocument()
