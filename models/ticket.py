# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    ticket_type_new_id = fields.Many2one('ticket.type', string='Ticket Type', tracking=True)
    ticket_category_id = fields.Many2one('ticket.category', string='Category', store=True, tracking=True)
    asset_id = fields.Many2one('itsm.asset', string='Asset Number', Tracking=True)
    categ = fields.Selection([
        ('hardware', 'Hardware'),
        ('software', 'Software'),
    ], string='Categ')