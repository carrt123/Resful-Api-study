from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.book_models import BooksModel


class TokenSchema(Schema):
    token = fields.String(required=True)


class BookRequestSchema(Schema):
    name = fields.String(required=True)
    author = fields.String(required=True)
    publish_time = fields.DateTime(required=True)


class BookModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BooksModel
        load_instance = True
