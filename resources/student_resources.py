from flask_restful import Resource
from resources import api


class StudentResource(Resource):
    def get(self, student_id: int):
        if student_id == 1:
            return {'id': student_id, 'name': 'Jack', 'gender': 'male'},200 #默认返回200，可以不用写
        else:
            return {'error': f'Student not found for id: {student_id}'},404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'Mary', 'gender': 'famale'}


#   '/students/<int: student_id>' 数据类型定义不要要加空格，直接连着写
api.add_resource(StudentResource, '/students/<int:student_id>')
