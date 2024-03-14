from flask_restful import Resource
from exts import api


class StudentResource(Resource):
    def get(self, student_id: int):
        if student_id == 1:
            return {'id': student_id, 'name': 'carrt', 'agent': 'boy'}, 200
        else:
            return {'error': f'Student not found for id: {student_id}'}, 404

    def post(self):
        pass

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'bob', 'agent': 'men'}


api.add_resource(StudentResource, '/students/<int:student_id>')
