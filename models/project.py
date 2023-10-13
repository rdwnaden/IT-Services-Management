# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    department_ids = fields.Many2many('hr.department', string='Department')
    