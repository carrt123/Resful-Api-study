from functools import wraps
from flask import request
from configs import LOGIN_SECRET
import jwt
from pathlib import Path


def token_required():
    def check_token(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            jwt_token = request.headers.get('token', None)
            if not jwt_token:
                return {"error": "User unauthorized"}, 404
            try:
                user_info = jwt.decode(jwt_token, LOGIN_SECRET, algorithms=["HS256"])
                if not user_info.get('username'):
                    return {'error': 'User unauthorized'}, 401
            except jwt.exceptions.DecodeError as error:
                return {'error': 'Invalid token'}, 401
            except jwt.exceptions.InvalidTokenError as error:
                return {'error': 'Invalid token'}, 401
            result = func(*args, **kwargs)
            return result

        return wrapper

    return check_token


# 返回到主目录下 attachment文件夹

def get_attachment_path():
    current_path = Path(__file__)
    parent_direction = current_path.parent
    attachment_path = parent_direction.joinpath("attachment")

    if not attachment_path.exists():
        try:
            attachment_path.mkdir(parents=True)
        except FileExistsError:
            pass  # 如果目录已存在，则不进行任何操作

    return attachment_path
