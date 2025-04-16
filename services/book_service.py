from sqlalchemy import Select, asc

from models.book_model import BookModel
from resources import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BookModel, book_id)

    def get_all_books(self):
        query = Select(BookModel).order_by(asc(BookModel.name))
        return db.session.scalars(query).all()

    def create_book(self, book_model: BookModel):
        db.session.add(book_model)
        db.session.commit()

        return book_model

    def update_book(self, book_id: int, book: BookModel):
        book_to_update = db.session.get(BookModel, book_id)
        book_to_update.name = book.name
        book_to_update.author = book.author
        book_to_update.year = book.year
        db.session.commit()
        return book_to_update

    def delete_book(self, book_id: int):
        book_to_delete = db.session.get(BookModel, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
