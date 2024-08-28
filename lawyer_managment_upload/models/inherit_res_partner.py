from odoo import fields ,models, api

class CustomerPartner(models.Model):
    _inherit = 'res.partner'

    #field relation between res partner and case model
    custom_id = fields.Many2one('case', string="Custom")






