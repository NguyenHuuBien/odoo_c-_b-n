from odoo import models, fields

class student(models.Model):
    _name = "manager_student"
    # _description = "abc"

    name = fields.Char(string="Name School")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    position = fields.Char(string="Position")

    manager_student_many = fields.Many2many("student", string="manager_student_many_1")