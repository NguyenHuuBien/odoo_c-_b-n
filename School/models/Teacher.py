from odoo import models, fields, api

class teacher(models.Model):
    _name = "teacher_model"

    name = fields.Char(string="Name Teacher")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", default="male")
    pay = fields.Float(string="Pay", compute="_total_pay", store=True, readonly=True)
    day_salary = fields.Float(string="Day", requied=True, store=True, groups="School.group_leader")
    salary = fields.Float(string="Salary", requied=True, store=True, groups="School.group_leader")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    list_student = fields.One2many("student_model", "name_teacher", string="List_student")
    # student_name = fields.One2many("student_model", string="Name_student")

    # không cho group_teacher nhập số lương
    # def write(self, vals):
    #     if not self.env.user.has_group('School.group_leader') and 'pay' in vals:
    #         raise UserError("You do not have permission to edit the 'pay' field.")
    #     return super(teacher, self).write(vals)
    
    # tính toán
    @api.depends("day_salary", "salary")
    def _total_pay(self):
        for product in self:
            product.pay = product.day_salary * product.salary
    
    # kiểm tra tính thay đôi
    @api.onchange("age", "day_salary", "salary")
    def _check_age_day_salary(self):
        if self.age < 0:
            self.age = None
        if self.day_salary < 0:
            self.day_salary = 0
        if self.salary < 0:
            self.salary = 0


    # def write(self, vals):
    #     # Kiểm tra xem người dùng có quyền sửa và không được sửa trường 'pay' hay không
    #     if not self.env.user.has_group('School.group_leader') and 'pay' in vals:
    #         raise UserError("You do not edit the 'pay' field.")
        
    #     old_pay = self.pay

    #     result = super(teacher, self).write(vals)

    #     if 'pay' in vals or (not self.env.user.has_group('School.group_leader') and self.pay != old_pay):
    #         self.pay = old_pay

    #     return result

    # student_id = fields.Many2one("student_model", string="student_id")


     # phân quyền cấp 3
    # cho_group_nào_nhìn_thấy = fields.Char(string="abc", groups="tên_module.goup_bạn_muốn_nó_thấy")

    # quan hệ
    # quan_hệ = fields.Many2one("tên_model_muốn_liên_hệ", string="dsadsa")