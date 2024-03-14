from sqlalchemy import Select, asc

from models.book_models import BooksModel
from exts import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BooksModel, book_id)

    def get_all_books(self):
        query = Select(BooksModel).order_by(asc(BooksModel.name))
        return db.session.scalars(query).all()

    def get_book_by_name(self, book_name: str):
        query = Select(BooksModel).where(BooksModel.name == book_name)
        return db.session.scalars(query).all()

    def create_book(self, book_model: BooksModel):
        exist_book_models = self.get_book_by_name(book_model.name)
        if exist_book_models:
            raise Exception('Book exists with name {}'.format(book_model.name))
        db.session.add(book_model)
        db.session.commit()

        return book_model

    def update_book(self, book_model: BooksModel):
        exist_book_model = self.get_book_by_id(book_model.id)
        # 不存在这本书进行报错
        if not exist_book_model:
            raise Exception('Mysql not Book id exists with {}'.format(book_model.id))
        else:
            # 判断是否传入字段对应的数据， 如果没有传入， 不修改字段对应数据
            if book_model.name:
                exist_book_model.name = book_model.name
            if book_model.author:
                exist_book_model.author = book_model.author
            if exist_book_model.publish_time:
                exist_book_model.publish_time = book_model.publish_time
        db.session.commit()
        return exist_book_model

    def delete_book(self, book_id: int):
        exist_book_model = self.get_book_by_id(book_id)
        if not exist_book_model:
            raise Exception('Mysql not Book id exists with {}'.format(book_id))
        else:
            db.session.delete(exist_book_model)
            db.session.commit()
