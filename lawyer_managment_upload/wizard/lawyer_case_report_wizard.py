from odoo import api, fields, models

class LawyerCaseReportWizard(models.TransientModel):
    _name = 'lawyer.case.report.wizard'
    _description = 'Lawyer Case Report Wizard'

    assigned_lawyer = fields.Many2one('lawyer', string='Lawyer', required=True)

    def action_print_report(self):
        # استرداد القضايا التي يعمل عليها المحامي
        cases = self.env['case'].search([
            ('assigned_lawyer', '=', self.assigned_lawyer.id)
        ])

        # توليد التقرير
        return self.env.ref('lawyer_managment.action_report_lawyer_case').report_action(cases)