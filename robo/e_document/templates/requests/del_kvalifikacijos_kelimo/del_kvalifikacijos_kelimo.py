# -*- coding: utf-8 -*-
from odoo import models, api


class EDocument(models.Model):
    _inherit = 'e.document'

    @api.multi
    def prasymas_del_kvalifikacijos_kelimo_workflow(self):
        self.ensure_one()
        generated_id = self.env['e.document'].create({
            'template_id': self.env.ref('e_document.isakymas_del_kvalifikacijos_kelimo_template').id,
            'document_type': 'isakymas',
            'employee_id2': self.employee_id1.id,
            'date_2': self.date_document,
            'date_3': self.date_3,
            'text_2': self.text_2,
            'text_3': self.text_3,
            'text_5': self.text_5,
            'user_id': self.user_id.id,
        })
        self.write({'record_model': 'e.document', 'record_id': generated_id.id})


EDocument()
