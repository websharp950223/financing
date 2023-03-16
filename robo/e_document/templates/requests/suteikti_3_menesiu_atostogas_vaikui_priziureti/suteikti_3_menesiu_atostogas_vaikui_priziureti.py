# -*- coding: utf-8 -*-
from odoo import models, api


class EDocument(models.Model):
    _inherit = 'e.document'

    @api.multi
    def prasymas_suteikti_3_menesiu_atostogas_vaikui_priziureti_workflow(self):
        self.ensure_one()
        generated_id = self.env['e.document'].create({
            'template_id': self.env.ref(
                'e_document.isakymas_del_3_menesiu_atostogu_vaikui_priziureti_suteikimo_template'
            ).id,
            'document_type': 'isakymas',
            'employee_id2': self.employee_id1.id,
            'date_1': self.date_1,
            'date_2': self.date_document,
            'user_id': self.user_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
        })
        self.write({'record_model': 'e.document', 'record_id': generated_id.id})


EDocument()
