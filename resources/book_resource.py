from datetime import datetime

from flask import request
from flask_restful import Resource

from models.book_model import BookModel
from resources import api
from services.book_service import BookService


class BookResource(Resource):
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return book_model.serialize()
        else:
            return {'error': f'Book not found for id: {book_id}'}, 404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'Mary', 'gender': 'famale'}


class BookListResource(Resource):
    def get(self):
        book_list = BookService().get_all_books()
        return [book_model.serialize() for book_model in book_list]

    def post(self):
        request_json = request.json
        if request_json:
            name = request_json.get('name')
            author = request_json.get('author')
            publish_time = datetime.fromisoformat(request_json.get('publish_time', None))

            book_model = BookModel(name=name, author=author, publish_time=publish_time)
            BookService().create_book(book_model)

            return book_model.serialize()
        else:
            return {'error': 'Please provide Book info as a Json'}, 400


api.add_resource(BookResource, '/books/<int:book_id>')
api.add_resource(BookListResource, '/books')
