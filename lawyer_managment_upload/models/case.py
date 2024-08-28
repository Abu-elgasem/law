from odoo import models,fields,api ,_
from odoo.exceptions import ValidationError

class Case(models.Model):
    _name = 'case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Case"

    case_name = fields.Char(string="Case Name")
    description = fields.Text(string="Description")
    partners_id = fields.Many2one('res.partner', string="Customer", required=True)
    date = fields.Date(string="Date")
    assigned_lawyer = fields.Many2one('lawyer', string="Assigned lawyer")
    product_document_ids = fields.One2many('document', 'custom_model_id', string="Documents")
    partners_ids = fields.One2many('res.partner', 'custom_id', string="Partnies")
    active = fields.Boolean(default=True)
    name = fields.Char(string="Order Reference",
                       required=True, copy=False,
                       readonly=False, index='trigram',
                       default=lambda self: _('New'))
    case_type_id = fields.Many2one('practice.area', string="Practice Area")
    State = fields.Selection([('open', 'Open'),
                              ('work_in_progress', 'Work in progress'),
                              ('done', 'Done'),
                              ('closed', 'Closed')], string="Status", default='open', tracking=True)
    date_of_judgment = fields.Datetime(string="Date of judgment")
    court_name = fields.Char(string="Court Name")
    judge = fields.Many2one('res.partner', string="Judge")
    court_docket_number = fields.Char(string="Court Docket Number")
    hearing_ids = fields.One2many('hearing.case', 'hearing_id', string="Hearing")
    lawyer_id = fields.Many2one('lawyer', string='Lawyer')

    @api.constrains('State', 'assigned_lawyer')
    def _check_assigned_lawyer(self):
        for rec in self:
            if rec.State == 'work_in_progress' and not rec.assigned_lawyer:
                raise ValidationError("You must assign a lawyer when the order is in 'Work in Progress' state.")


    #creates  a sequential name set
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order'])
                ) if 'date_order' in vals else None
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'case', sequence_date=seq_date) or _("New")
        return super().create(vals_list)



    def action_work_in_progress(self):
        for rec in self:
            rec.State = 'work_in_progress'

    def action_closed(self):
        for rec in self:
            rec.State = 'closed'

    def action_done(self):
        for rec in self:
            if rec.State != 'done':
                # قم بإنشاء الفاتورة
                invoice = self.env['account.move'].create({
                    'move_type': 'out_invoice',
                    'partner_id': rec.partners_id.id,
                    'invoice_date': fields.Date.today(),
                    'invoice_line_ids': [
                        (0, 0, {
                            'name' : rec.case_name,
                            'quantity' : 1.0,
                            'price_unit' : 100.0,  # يمكنك تخصيص السعر هنا أو جلبه من المنتج المرتبط بالقضية
                        }),
                    ],
                })

                # تحديث حالة السجل إلى "done"
                rec.State = 'done'

                # تصديق الفاتورة
                invoice.action_post()
            else:
                raise ValidationError("The case is already done.")










