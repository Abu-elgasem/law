from odoo import models, fields, api

class InheritHrEmployee(models.Model):
    _inherit = 'hr.employee'

    ban = fields.Char(string="BAN")
    practice_area_ids = fields.Many2many('practice.area', string="Practice Area")
    is_lawyer_created = fields.Boolean(string="Lawyer Created", default=False)
    lawyer_id = fields.Many2one('lawyer', string="Employee")


    def action_create_lawyer_profile(self):
        for employee in self:
            # Search for an existing custom record linked to this employee
            custom_record = self.env['lawyer'].search([('employee_id', '=', employee.id)], limit=1)
            # Prepare the values to be created/updated
            custom_record_vals = {
                'name': employee.name,
                'gender': employee.gender,
                'mobile': employee.mobile_phone,
                'image': employee.image_128,
                'practice_area_ids': [(6, 0, employee.practice_area_ids.ids)],  # Many2many field update
                'email': employee.work_email,
                'company_id': employee.company_id.id,  # Note: 'company_id' not 'copmany_id'
                'active': employee.active,
                # Add more fields as needed
            }
            if not custom_record:
                # Create a new custom record
                custom_record_vals['employee_id'] = employee.id  # Ensure the relationship is established
                self.env['lawyer'].create(custom_record_vals)
            else:
                # Update the existing custom record
                custom_record.write(custom_record_vals)

            self.is_lawyer_created = True

    def write(self, custom_record_vals):
        for employee in self:
            res = super(InheritHrEmployee, self).write(custom_record_vals)
            if self.is_lawyer_created:
                custom_record = self.env['lawyer'].search([('employee_id', '=', employee.id)], limit=1)
                custom_record_vals = {
                    'name' : employee.name,
                    'gender' : employee.gender,
                    'mobile' : employee.mobile_phone,
                    'image' : employee.image_128,
                    'practice_area_ids' : [(6, 0, employee.practice_area_ids.ids)],  # Many2many field update
                    'email' : employee.work_email,
                    'company_id' : employee.company_id.id,  # Note: 'company_id' not 'copmany_id'
                    'active' : employee.active,
                    # Add more fields as needed
                }
                if custom_record:
                    custom_record.write(custom_record_vals)
           # return res

