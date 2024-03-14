from datetime import datetime
from flask_restful import Resource
from flask_apispec import doc, MethodResource, use_kwargs, marshal_with
from utils import token_required
from exts import api, docs
from services.book_service import BookService
from flask import request
from models.book_models import BooksModel
from schemas.book_schema import TokenSchema, BookRequestSchema, BookModelSchema


class BooksResource(MethodResource, Resource):
    @doc(description="Get book's information", tags=['Book Requests'])
    @marshal_with(BookModelSchema, code=200)  # code=200 当return 状态为200 才调用BookModelSchema函数
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id=book_id)
        if book_model:
            return book_model
        else:
            return {'error': 'Student not found for id: {book_id}'}, 404

    @doc(description="Update book's information", tags=['Book Requests']) # 在swagger 描述此函数的作用
    @use_kwargs(BookRequestSchema, location='json')  # 在json里， 按照BookRequestSchema定义提取参数
    @use_kwargs(TokenSchema, location='headers')      # 在headers 按照TokenSchema 定义提取参数
    @token_required()
    def put(self, book_id: int, **kwargs):
        name = kwargs.get('name', None)
        author = kwargs.get('author', None)
        publish_time = kwargs.get('publish_time', None)

        book_model = BooksModel(id=book_id, name=name, author=author, publish_time=publish_time)
        book_model = BookService().update_book(book_model)

        return book_model.serialize()

    @doc(description="Delete book's information", tags=['Book Requests'])
    def delete(self, book_id: int):
        try:
            BookService().delete_book(book_id)
            return {'success': 'Already delete the Book id with {}'.format(book_id)}
        except Exception as error:
            return {'error': '{}'.format(error)}


class BooksCRUDResource(MethodResource, Resource):
    @doc(description="Get all book's information", tags=['Books Requests'])
    def get(self):
        book_list = BookService().get_all_books()
        return [book_model.serialize() for book_model in book_list]

    @doc(description="Add a book's information", tags=['Books Requests'])
    @token_required()
    def post(self):
        try:
            request_json = request.json
            if request_json:
                name = request_json.get('name', None)
                author = request_json.get('author', None)
                publish_time = datetime.fromisoformat(request_json.get('publish_time', None))

                book_model = BooksModel(name=name, author=author, publish_time=publish_time)
                BookService().create_book(book_model)

                return book_model.serialize()
            else:
                return {"error": "Please provide book info as a json"}, 404
        except Exception as error:
            return {'error': '{}'.format(error)}


api.add_resource(BooksResource, '/books/<int:book_id>')
api.add_resource(BooksCRUDResource, '/books')

docs.register(BooksResource)
docs.register(BooksCRUDResource)
