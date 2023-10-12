# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Services(models.Model):
    _name = 'itsm.services'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Services'

    name = fields.Char('Form Number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'),)
    part_id = fields.Many2one('itsm.part', string='Part Name', tracking=True)
    services_date = fields.Date('Services Date', tracking=True)
    description = fields.Text('Description', tracking=True)
    asset_id = fields.Many2one('itsm.asset', string='Asset Number', tracking=True)
    company_id = fields.Many2one('res.company', string='Company', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default = 'draft', tracking=True)

    @api.model
    def create(self, vals):
        seq_date = None
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('itsm.services') or _('New')
        result = super(Services, self).create(vals)
        return result

    def action_confirm(self):
        self.state = 'waiting_approval'

    def action_set_draft(self):
        self.state = 'draft'

    def action_approved(self):
        self.state = 'approved'

    def action_rejected(self):
        self.state = 'rejected'



    