from flask_restful import Resource

from configs import LOGIN_SECRET
from exts import api
from models.user_models import UsersModel
from flask import request
from services.user_service import UserService
import jwt


class LoginResource(Resource):
    def post(self):
        try:
            request_json = request.json
            if request_json:
                username = request_json.get('username', 'None')
                password = request_json.get('password', 'None')
                user_model = UserService().login(username=username, password=password)

                if user_model:
                    user_json = user_model.serialize()
                    jwt_token = jwt.encode(user_json, LOGIN_SECRET, algorithm='HS256')
                    user_json['token'] = jwt_token
                    return user_json

                else:
                    return {"error": "username or password error"}, 401
            else:
                return {'error': "Please provide username and password info as a json"}, 400
        except Exception as error:
            return {'error': '{}'.format(error)}, 400


api.add_resource(LoginResource, '/login')
