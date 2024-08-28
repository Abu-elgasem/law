# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name' : 'Lawyer Managment' ,
    'version' : '1.2',
    'sequence': 16,
    'category' : 'Legal',
    'summary' : 'Comprehensive system for managing law firms and cases',
    'description': """
        Lawyer Management System
            ========================
                A comprehensive module designed to manage law firms, including case management,
                     lawyer assignments, court schedules, client interactions, and document management.
        """,
    'author' : 'Abuelgasem',
    'depends' : ['base','base_setup',
                 'hr','mail', 'contacts','sale',
                 'product',] ,
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/lawyer_view.xml',
        'views/inherit_hr_employee_view.xml',
        'data/sequence_data.xml',
        'views/case_view.xml',
        'views/inherit_prudoct_template_view.xml',
        'views/inhert_sale_orde_view.xml',
        'wizard/case_report_wizard_menu.xml',
        'wizard/case_report_wizard_view.xml',
        'wizard/lawyer_case_report_wizard_menu.xml',
        'wizard/lawyer_case_report_wizard_views.xml',
        'report/report_case_template.xml',
        'report/report_lawyer_case_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',

}