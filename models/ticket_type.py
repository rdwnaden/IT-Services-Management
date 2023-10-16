# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ticket_type(models.Model):
    _name = 'ticket.type'

    name = fields.Char(string='Name')
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]