# -*- coding: utf-8 -*-
from odoo import models, api


class EDocument(models.Model):
    _inherit = 'e.document'

    @api.multi
    def prasymas_atleisti_nuo_darbo_valstybinems_visuomeninems_pareigoms_atlikti_workflow(self):
        self.ensure_one()
        generated_id = self.env['e.document'].create({
            'template_id': self.env.ref(
                'e_document.isakymas_atleisti_nuo_darbo_valstybinems_(visuomeninems)_pareigoms_atlikti_template'
            ).id,
            'document_type': 'isakymas',
            'employee_id2': self.employee_id1.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'date_2': self.date_document,
            'user_id': self.user_id.id,
            'text_1': self.text_3,
            'text_2': self.text_4,
        })
        self.write({'record_model': 'e.document', 'record_id': generated_id.id})


EDocument()
