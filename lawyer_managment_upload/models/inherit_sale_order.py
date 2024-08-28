from odoo import models, api, fields
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    assigned_lawyer = fields.Many2one('lawyer', string="Assigned lawyer")

    State = fields.Selection([('open', 'Open'),
                              ('work_in_progress', 'Work in progress'),
                              ('closed', 'Closed')],
                             string='Status', readonly=True, default='open')

    @api.constrains('State', 'assigned_lawyer')
    def _check_assigned_lawyer(self) :
        for order in self :
            if order.State == 'work_in_progress' and not order.assigned_lawyer :
                raise ValidationError("You must assign a lawyer when the order is in 'Work in Progress' state.")
    @api.model
    def create_custom_record(self, partner_id, date, lawyer_id):
        lawyer = self.env['lawyer'].browse(lawyer_id)
        for order in self:
            for order_line in order.order_line:
                self.env['case'].create({
                    'partners_id': partner_id,
                    'assigned_lawyer': lawyer.id,
                    'date': date,
                    'case_name': order_line.product_template_id.name,
                    # Add more fields as needed
                })

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id.required_case:
                    self.create_custom_record(order.partner_id.id, order.date_order, order.assigned_lawyer.id)
                    break

        return True