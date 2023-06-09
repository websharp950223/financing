# -*- coding: utf-8 -*-
{
    'name' : 'Gemma',
    'version' : '1.0',
    'description': """
        Papildinys klientui "Gemma"
                """,
    'author' : 'Robolabs',
    'website': 'http://www.robolabs.lt',
    'license': 'Other proprietary',
    'depends': ['work_schedule', 'l10n_lt_payroll', 'e_document'],
    'data': [
        'data/accounting_data.xml',
        'data/config_parameters.xml',
        'data/cron_jobs.xml',
        'data/l10n_lt_hr_payroll_data.xml',
        'data/e_document_template.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/robo_header.xml',
        'views/du_aspi_export_wizard.xml',
        'views/gemma_cash_register.xml',
        'views/gemma_data_import.xml',
        'views/gemma_invoice.xml',
        'views/gemma_payment.xml',
        'views/gemma_payment_type.xml',
        'views/gemma_sale_line.xml',
        'views/gemma_xls_wizard.xml',
        'views/hr_employee.xml',
        'views/robo_company_settings.xml',
        'views/account_bank_statement_line.xml',
        'wizard/polis_real_time_fetcher.xml',
        'views/menuitems.xml',
        'views/report.xml',
        'views/res_partner.xml',
        'views/hr_employee_bonus_views.xml',
        'templates/orders/del_priedo_skyrimo_grupei/del_priedo_skyrimo_grupei.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
}