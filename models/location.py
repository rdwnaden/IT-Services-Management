# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _name = 'itsm.location'
    _description = 'Location'

    name = fields.Char(string='Name')
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]