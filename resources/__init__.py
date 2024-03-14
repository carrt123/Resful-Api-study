from flask import Flask, Response
from exts import api, db, migrate, docs, swagger
from models.book_models import BooksModel
from models.user_models import UsersModel
import configs
import click
from fakes import fake_book, fake_user

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Flask Restful API project',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SPEC_URL': '/swagger',
        'APISPEC_SPEC_UI_URL': '/swagger-ui'
    })
    register_resources()
    register_extensions(app)
    register_fake(app)
    register_yaml(app)

    return app


def register_extensions(app):
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    docs.init_app(app)


def register_resources():
    from resources import student_resources, book_resources, user_resources, attachment_resources


def register_fake(app):
    @app.cli.command()
    @click.option('--nums1', default=10, help='Quality of book, default is 10.')
    @click.option('--nums2', default=10, help='Quality of user, default is 10.')
    def forge(nums1, nums2):
        db.drop_all()
        db.create_all()
        fake_book(nums1)
        fake_user(nums2)


def register_yaml(app):
    @app.route('/swagger.yaml')
    def generate_swagger_yaml():
        yaml_doc = docs.spec.to_yaml()
        return Response(yaml_doc, mimetype="text/yaml")
