from odoo import fields,models,api

class PracticeArea(models.Model):
    _name = 'practice.area'
    _description = " Practice Area"

    name = fields.Char(string="Name")