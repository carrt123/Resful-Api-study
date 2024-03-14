from models.book_models import BooksModel
from models.user_models import UsersModel
from exts import db
from faker import Faker
import os
fake = Faker()


def fake_book(nums):
    BooksModel.query.delete()
    db.create_all()

    for i in range(nums):
        book = BooksModel(
            name=fake.word(),
            author=fake.name(),
            publish_time=fake.date_time_this_year(),
        )
        db.session.add(book)
    db.session.commit()


def fake_user(nums):
    UsersModel.query.delete()
    user = UsersModel(username='Bob')
    user.set_password('123456789')
    db.session.add(user)
    for i in range(nums):
        user = UsersModel(username=fake.name())
        user.set_password('123456789')
        db.session.add(user)
    db.session.commit()
