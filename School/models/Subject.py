from odoo import models, fields

class subject(models.Model):
    _name = "subject_model"

    name = fields.Char(string="Name subject")
    many_student = fields.Many2many("student_model", string="Many_student")
