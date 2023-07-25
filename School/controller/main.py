from odoo import http
from odoo.http import request
import json
# from odoo.exceptions import UserError
# from flask import jsonify

class MyController(http.Controller):

    # def validate(data, all_fields):
    #     keys = data.keys()

    #     for key in keys:
    #         if key not in all_fields:
    #             raise UserError("field not in Model") 

    @http.route('/api/my_model', type='http', auth='public', csrf=False, methods=['GET'], website="False")
    def get_my_model(self, **kw):
        records = request.env['student_model'].sudo().search([])
        data = []
        for record in records:
            data.append({
                "name": record.name,
                "age": record.age,
                "name_teacher": record.name_teacher.name,
                "many_subject": [subject.name for subject in record.many_subject],
            })
        return http.Response(json.dumps(data), content_type='application/json')

    @http.route('/api/my_model/<int:id>', type='json', auth='public', csrf=False, methods=['GET'], website="False")
    def get_my_model_record(self, id, **kw):
        records = request.env['student_model'].sudo().search([('id', '=', id)])
        if not records:
            return {"error" : "Not found id"}
        else:
            data = {
                    "name": records.name,
                    "age": records.age,
                    "name_teacher": records.name_teacher.name,
                    "many_subject": [subject.name for subject in records.many_subject],
                }
            return json.dumps(data)

    @http.route('/api/my_model', type='json', auth='public', csrf=False, methods=['POST'], website="False")
    def create_my_model(self, **kw):
        if kw:
            # Tạo bản ghi mới
            record = request.env['student_model'].sudo().create({
                'name': kw.get('name'),
                'age': kw.get('age'),
                'name_teacher': kw.get('name_teacher'),
                'many_subject': [(6, 0, kw.get('many_subject'))]
            })
            # Đọc thông tin bản ghi mới tạo
            new_record_data = record.read(["id", "name", "age", "name_teacher", "many_subject"])[0]

            # Trả về thông tin bản ghi mới tạo
            return json.dumps(new_record_data)  
        else:
            return json.dumps({"error": "Missing data"})

    @http.route('/api/my_model/<int:id>', type='json', auth='public', csrf=False, methods=['PUT'])
    def update_my_model(self, id, **kw):
        record = request.env['student_model'].sudo().search([('id', '=', id)])  

        if not record:
            return {'message': "not found"}
        else:
            record.write(kw)
            data = record.read(["id", 'name'])
            return json.dumps(data)

    @http.route('/api/my_model/<int:id>', type='json', auth='public', csrf=False, methods=['DELETE'])
    def delete_my_model(self, id, **kw):
        record = request.env['student_model'].sudo().search([('id', '=', id)])
        if record:
            record.unlink()
            return {'success': True}
        else:
            return {'error': 'Record not found'}



    