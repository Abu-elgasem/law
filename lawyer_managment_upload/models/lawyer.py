from odoo import models, fields, api

class Lawyer(models.Model):
    _name = 'lawyer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Lawyer Managment"

    employee_id = fields.Many2one('hr.employee', string='Employee')
    name = fields.Char(string="Name")
    mobile = fields.Char(string="Mobile")
    company_id = fields.Many2one('res.company')
    gender = fields.Selection([('male', 'Male'), ('FEmale', 'Female')], string="Gender")
    birth_date = fields.Date(string="Birth Date")
    image = fields.Binary("Image", attachment=True)
    practice_area_ids = fields.Many2many('practice.area', string="Practice Area")
    email = fields.Char(string="Email")
    active = fields.Boolean(default=True)
    case_ids = fields.One2many('case', 'lawyer_id', string='Cases')
