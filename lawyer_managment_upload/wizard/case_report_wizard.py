from odoo import api, fields, models

class CaseReportWizard(models.TransientModel):
    _name = 'case.report.wizard'
    _description = 'Case Report Wizard'

    date_from = fields.Date(string='From Date', required=True)
    date_to = fields.Date(string='To Date', required=True)

    def action_print_report(self):
        # استرداد الحالات المفتوحة في الفترة المحددة
        cases = self.env['case'].search([
            ('State', '=', 'open'),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
        ])

        # توليد التقرير
        return self.env.ref('lawyer_managment.action_report_case').report_action(cases)
