# -*- coding: utf-8 -*-
{
    'name' : 'Raso Retail',
    'version' : '1.0',
    'description': """
        Papildinys klientui "RASO RETAIL"
                """,
    'author' : 'Robolabs',
    'website': 'http://www.robolabs.lt',
    'license': 'Other proprietary',
    'depends': ['robo_stock'],
    'data': [
        'data/accounting_data.xml',
        'data/config_parameters.xml',
        'data/cron_jobs.xml',
        'views/menus.xml',
        'views/product_category.xml',
        'views/product_category_discounts.xml',
        'views/product_template.xml',
        'views/product_template_discounts.xml',
        'views/product_template_prices.xml',
        'views/raso_invoices.xml',
        'views/raso_invoices_line.xml',
        'views/raso_payment_type.xml',
        'views/raso_payments.xml',
        'views/raso_sales.xml',
        'views/raso_shoplist.xml',
        'views/raso_shoplist_registers.xml',
        'views/res_partner.xml',
        'views/robo_company_settings.xml',
        'wizard/raso_export_wizard.xml',
        'wizard/raso_import_wizard.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
}