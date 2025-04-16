from sqlalchemy import Select, asc

from models.book_model import BookModel
from resources import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BookModel, book_id)

    def get_all_books(self):
        query = Select(BookModel).order_by(asc(BookModel.name))
        return db.session.scalars(query).all()

    def get_book_by_name(self, book_name: str):
        query = Select(BookModel).where(BookModel.name == book_name)
        return db.session.scalars(query).all()

    def create_book(self, book_model: BookModel):
        exist_books = self.get_book_by_name(book_model.name)
        if exist_books:
            raise Exception(f'Book with name “ {book_model.name} ”already exists')

        db.session.add(book_model)
        db.session.commit()

        return book_model

    def update_book(self, book_models: BookModel):
        exsit_book = self.get_book_by_id(book_models.id)
        if not exsit_book:
            raise Exception(f'Book with id “ {book_models.id} ” not found')

        if book_models.name:
            exsit_book.name = book_models.name
        if book_models.author:
            exsit_book.author = book_models.author
        if book_models.publish_time:
            exsit_book.publish_time = book_models.publish_time

        db.session.commit()

        return exsit_book

    def delete_book(self, book_id: int):
        book_to_delete = db.session.get(BookModel, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
