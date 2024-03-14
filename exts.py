# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apispec import FlaskApiSpec
from flask_restful_swagger_3 import Api, swagger

api = Api()
db = SQLAlchemy()
migrate = Migrate()
docs = FlaskApiSpec()
