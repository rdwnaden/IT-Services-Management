# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Brands(models.Model):
    _name = 'itsm.brands'
    _description = 'Brands'

    name = fields.Char(string='Name')
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]
    