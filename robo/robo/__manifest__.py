# -*- coding: utf-8 -*-
# (c) 2021 Robolabs

{
    'name': 'RoboLabs Pages',
    'version': '1.0',
    'author': 'Robolabs',
    'website': 'http://www.robolabs.lt',
    'license': 'Other proprietary',
    'category': 'Reporting',
    'description': """
Lets the user create a custom dashboard.
========================================

Allows users to create custom dashboard.
    """,
    'depends': ['robo_theme_v10', 'avansine_apyskaita', 'due_payments', 'sodra', 'mass_mailing',
                'account_analytic_default', 'robo_core'],
    'data': [
        'data/ir_actions_client.xml',
        'data/ir_ui_menu.xml',
        'data/robo_header.xml',
        'data/mail_channel.xml',
        'data/mail_message_subtype.xml',
        'data/hr_department.xml',
        'data/mail_templates.xml',
        'data/ir_actions_act_window_settings.xml',
        'data/emojii.xml',

        'security/ir_module_category.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record.rules.xml',

        'wizard/register_payment_views.xml',

        'views/assets.xml',
        'views/left_menu_templates.xml',
        'views/res_users_views.xml',
        'views/robo_upload_views.xml',
        'views/product_template_views.xml',
        'views/account_bank_statement_views.xml',
        'views/ir_ui_view_views.xml',
        'views/ir_actions_server_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_actions_report_xml_views.xml',
        'views/ir_actions_act_window_views.xml',
        'views/ir_ui_menu_views.xml',
        'views/ir_module_module_views.xml',
        'wizard/account_bank_statement_merge_wizard_views.xml',
        'views/base_templates.xml',
        'views/res_partner_bank_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_employee_child_views.xml',
        'views/schedule_template_views.xml',
        'views/hr_contract_appointment_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_holidays_views.xml',
        'views/kita.xml',
        'views/res_partner_views.xml',
        'views/account_payment_views.xml',
        'views/hr_contract_views.xml',
        'views/front_bank_statement_views.xml',
        'views/front_bank_statement_line_views.xml',
        'views/hr_employee_payment_views.xml',
        'views/account_move_views.xml',

        'views/mail_channel_views.xml',
        'views/mail_message_views.xml',
        'views/account_journal_views.xml',
        'views/res_company_vat_status_views.xml',
        'views/res_company_shareholder_views.xml',
        'views/hr_department_views.xml',
        'views/crm_team_views.xml',
        'views/hr_job_views.xml',
        'views/category_mapping_views.xml',
        'views/res_company_views.xml',
        'views/zero_npd_period_views.xml',
        'views/res_company_message_views.xml',
        'data/product.category.csv',
        'views/periodic_invoice_views.xml',
        'views/periodic_front_bank_statement.xml',
        'views/cash_receipt_views.xml',
        'views/mail_template_views.xml',
        'views/client_support_ticket_views.xml',
        'views/account_invoice_views.xml',
        'views/hr_expense_views.xml',
        'views/account_invoice_tags_views.xml',
        'views/account_move_line_views.xml',
        'views/paypal_api_views.xml',
        'views/revolut_api_views.xml',
        'views/robo_report_job_views.xml',
        'views/robo_import_job_views.xml',
        'views/robo_front_extend/sepa.xml',
        'views/enable_banking_connector_views.xml',
        'views/braintree_gateway_views.xml',
        'views/braintree_transaction_views.xml',
        'views/braintree_customer_views.xml',
        'views/braintree_merchant_account_views.xml',
        'views/braintree_configuration_views.xml',
        'views/account_analytic_account_views.xml',

        'wizard/start_employee_internship_view.xml',
        'wizard/account_invoice_tax_change_wizard.xml',
        'wizard/res_users_chart_settings/res_users_chart_settings.xml',
        'wizard/account_invoice_partner_change_wizard.xml',
        'wizard/analytic_wizard/account_move_line_analytic_wizard.xml',
        'wizard/analytic_wizard/account_move_line_change_analytics_wizard.xml',
        'wizard/analytic_wizard/invoice_analytic_wizard_all.xml',
        'wizard/analytic_wizard/invoice_analytic_wizard_line.xml',
        'wizard/invoice_mass_mailing/invoice_mass_mailing_wizard.xml',
        'wizard/account_invoice_type_change_wizard.xml',
        'wizard/report_invoice_processing_issue_views.xml',
        'wizard/ap_employee_select_wizard_views.xml',
        'wizard/account_invoice_refund_views.xml',
        'wizard/account_invoice_number_wizard_views.xml',
        'wizard/account_invoice_vat_change_wizard_views.xml',
        'wizard/invoice_change_line_wizard_views.xml',
        'wizard/invoice_change_tax_line_wizard_views.xml',
        'wizard/cash_receipt_number_wizard_views.xml',
        'wizard/account_aged_trial_balance_views.xml',
        'wizard/invoice_registry_wizard_views.xml',
        'wizard/payslips_report_wizard_views.xml',
        'wizard/timesheets_report_wizard_views.xml',
        'wizard/atostoginiu_kaupiniu_wizard_views.xml',
        'wizard/client_support_ticket_wizard_views.xml',
        'wizard/expenses_wizard_view.xml',
        'wizard/print_contract_wizard_views.xml',
        'wizard/auto_process_reconciliation_views.xml',
        'wizard/robo_materialized_view_wizard.xml',
        'wizard/base_partner_merge_automatic_wizard_views.xml',
        'wizard/employee_count_report_views.xml',
        'wizard/mail_channel_subscriptions_wizard_views.xml',
        'wizard/mail_compose_message_views.xml',
        'wizard/needaction_ceo_wizard_views.xml',
        'wizard/needaction_accountant_wizard_views.xml',
        'wizard/overpay_transfer_request_wizard_views.xml',
        'wizard/robo_company_settings_views.xml',
        'wizard/robo_mail_compose_message_views.xml',
        'wizard/invoice_financial_account_change_wizard_views.xml',
        'wizard/downtime_report_views.xml',
        'wizard/front_bank_statement_merge_wizard_views.xml',
        'wizard/invoice_date_change_wizard_views.xml',
        'wizard/hr_employee_work_norm_report_export_views.xml',
        'wizard/change_user_partner_of_employee_wizard_views.xml',

        'report/account_invoice_report_materialized_views.xml',
        'report/report_robo_report_employee_contract_templates.xml',
        'report/account_invoice_report_views.xml',
        'report/account_cashflow_report_views.xml',
        'report/accounting_report_views.xml',
        'report/hr_holidays_report_views.xml',
        'report/kasos_knyga_report_views.xml',
        'report/account_report_general_ledger_views.xml',
        'report/report_contract_termination_attachment_templates.xml',
        'report/report_overpay_transfer_request_templates.xml',

        'data/ir_cron.xml',
        'data/robo_header_items.xml',
        'data/robo_header_action_switchers.xml',
    ],
    'qweb': ['static/src/xml/*.xml', 'static/src/xml/menu_left/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,

}
