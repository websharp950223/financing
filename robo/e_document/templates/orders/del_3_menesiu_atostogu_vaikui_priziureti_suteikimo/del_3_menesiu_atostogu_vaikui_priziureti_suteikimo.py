# -*- coding: utf-8 -*-
from odoo import models, api


class EDocument(models.Model):
    _inherit = 'e.document'

    @api.multi
    def isakymas_del_3_menesiu_atostogu_vaikui_priziureti_suteikimo_workflow(self):
        self.ensure_one()
        skip = self.check_skip_leave_creation()
        if not skip:
            hol_id = self.env['hr.holidays'].create({
                'name': 'Trijų mėnesių atostogos vaikui prižiūrėti',
                'data': self.date_document,
                'employee_id': self.employee_id2.id,
                'holiday_status_id': self.env.ref('hr_holidays.holiday_status_TM').id,
                'date_from': self.calc_date_from(self.date_from),
                'date_to': self.calc_date_to(self.date_to),
                'type': 'remove',
                'numeris': self.document_number,
            })
            hol_id.action_approve()
            self.inform_about_creation(hol_id)
            self.write({
                'record_model': 'hr.holidays',
                'record_id': hol_id.id,
            })


EDocument()
