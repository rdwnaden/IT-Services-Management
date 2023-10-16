# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ticket_category(models.Model):
    _name = 'ticket.category'

    name = fields.Char(string='Name')
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]