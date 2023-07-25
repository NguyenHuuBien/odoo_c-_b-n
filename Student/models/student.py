from odoo import models, fields

class student(models.Model):
    _name = "student"
    # _description = "abc"

    name = fields.Char(string="Name School")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    # manager_student_id = fields.Many2one("manager_student", string="manager_student_id")
    manager_student_many = fields.Many2many("manager_student", string="manager_student_many")
    # phân quyền cấp 3
    # cho_group_nào_nhìn_thấy = fields.Char(string="abc", groups="tên_module.goup_bạn_muốn_nó_thấy")

    # gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], requied=True, string="Gender", default='male')


    # quan hệ
    # quan_hệ = fields.Many2one("tên_model_muốn_liên_hệ", string="dsadsa")
