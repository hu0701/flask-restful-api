from datetime import datetime

from flask import request, Response
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from common.api_tools import token_required
from models.book_model import BookModel
from resources import app, api, docs
from services.book_service import BookService


class BookResource(MethodResource, Resource):  # 功能：获取单个书籍信息、更新书籍信息
    @doc(description='Get a book info by id', tage=['Book Resource'])
    def get(self, book_id: int):  # 功能：获取单个书籍信息
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return book_model.serialize()
        else:
            return {'error': f'Book not found for id: {book_id}'}, 404

    @doc(description='Get a book info by id', tage=['Book Resource'])
    @token_required()
    def put(self, book_id: int):  # 功能：更新书籍信息
        try:
            request_json = request.json
            if request_json:
                name = request_json.get('name')
                author = request_json.get('author')
                publish_time_str = request_json.get('publish_time', None)
                publish_time = datetime.fromisoformat(publish_time_str) if publish_time_str else None

                book_model = BookModel(id=book_id, name=name, author=author, publish_time=publish_time)
                book_model = BookService().update_book(book_model)

                return book_model.serialize()
            else:
                return {'error': 'Please provide Book info as a Json'}, 400
        except Exception as error:
            return {'error': 'f'(error)}, 400


class BookListResource(Resource):  # 功能：获取所有书籍信息、创建书籍信息
    def get(self):
        book_list = BookService().get_all_books()
        return [book_model.serialize() for book_model in book_list]

    @token_required()  # 来检查用户是否已认证
    def post(self):
        try:
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
        except Exception as error:
            return {'error': str(error)}, 500


api.add_resource(BookResource, '/books/<int:book_id>')  # 功能：添加资源路由，其中book_id是动态参数
api.add_resource(BookListResource, '/books')  # 功能：添加资源路由

docs.register(BookResource)  # 注册BookResource类到docs对象中


@app.route('/swagger.yaml', methods=['GET'])
def gen_swagger_yaml():
    yaml_spec = docs.spec.to_yaml()
    return Response(yaml_spec, mimetype='text/yaml')
