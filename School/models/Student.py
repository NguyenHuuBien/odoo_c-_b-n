from odoo import models, fields, api

class student(models.Model):
    _name = "student_model"

    name = fields.Char(string="Name student")
    age = fields.Integer(string="Age", default = 0)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", default="male")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    name_teacher = fields.Many2one("teacher_model", string="Name_teacher")
    many_subject = fields.Many2many("subject_model", string="Many_subject")

