from sqlalchemy import Select, asc

from models.user_models import UsersModel
from exts import db


class UserService:

    def login(self, username: str, password: str):

        user_model = UsersModel.query.filter_by(username=username).first()

        # 判断用户是否存在并且密码验证通过

        if user_model and user_model.validate_password(password):
            return user_model
        else:
            raise Exception('None')
