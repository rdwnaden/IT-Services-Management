# -*- coding: utf-8 -*-

from odoo import models, fields, api


class part(models.Model):
    _name = 'itsm.part'
    _description = 'Part'

    name = fields.Char(string='Part Name')
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]