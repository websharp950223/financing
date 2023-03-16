# -*- coding: utf-8 -*-
{
    'name': 'rKeeper Integration',
    'version': '1.0',
    'description': """
        rKeeper Integration
                """,
    'author': 'Robolabs',
    'website': 'http://www.robolabs.lt',
    'license': 'Other proprietary',
    'depends': ['robo_mrp'],
    'data': [
        'data/ir_cron.xml',
        'data/ir_config_parameter.xml',
        'data/r_keeper_configuration.xml',
        'data/robo_header.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/r_keeper_views/r_keeper_data_import_job_views.xml',
        'views/r_keeper_views/r_keeper_data_export_views.xml',
        'views/r_keeper_views/r_keeper_sale_line_views.xml',
        'views/r_keeper_views/r_keeper_payment_views.xml',
        'views/r_keeper_views/r_keeper_payment_type_views.xml',
        'views/r_keeper_views/r_keeper_point_of_sale_views.xml',
        'views/r_keeper_views/r_keeper_point_of_sale_product_views.xml',
        'views/r_keeper_views/r_keeper_configuration_views.xml',
        'views/r_keeper_views/r_keeper_product_tax_mapper_views.xml',
        'views/r_keeper_views/r_keeper_modifier_views.xml',
        'views/r_keeper_views/r_keeper_modifier_rule_views.xml',
        'views/base_views/product_template_views.xml',
        'views/base_views/product_category_views.xml',
        'views/base_views/stock_inventory_views.xml',
        'wizard/robo_company_settings_views.xml',
        'wizard/r_keeper_xml_import_wizard_views.xml',
        'wizard/r_keeper_xls_import_wizard_views.xml',
        'wizard/r_keeper_pos_transfer_wizard_views.xml',
        'wizard/r_keeper_pos_update_wizard_views.xml',
        'wizard/r_keeper_data_export_wizard_views.xml',
        'data/robo_header_items.xml',  # Uses action defined in views, thus at the bottom
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
}