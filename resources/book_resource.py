from datetime import datetime

from flask import request, Response
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from common.api_tools import token_required
from models.book_model import BookModel
from resources import app, api, docs
from services.book_service import BookService


class TokeSchema(Schema):
    token = fields.String(required=True)


class BookRequestSchema(Schema):
    name = fields.String(required=True)
    author = fields.String(required=True)
    publish_time = fields.DateTime(required=True)


class BookResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True


class BookResource(MethodResource, Resource):  # 功能：获取单个书籍信息、更新书籍信息, MethodResource与@doc结合使用
    @doc(description='Get a book info by id', tags=['Book Resource'], params={'book_id': {'description': '图书ID', 'required': True}})       # @doc用于描述API接口
    @marshal_with(BookResponseSchema, code=200)  # @marshal_with用于序列化返回结果
    def get(self, book_id: int):  # 功能：获取单个书籍信息
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return book_model, 200
        else:
            return {'error': f'Book not found for id: {book_id}'}, 404

    @doc(description='Update a book info by id', tags=['Book Resource'])
    @use_kwargs(BookRequestSchema, location='json')  # @use_kwargs用于解析请求参数
    @use_kwargs(TokeSchema, location='headers')  # @use_kwargs用于解析请求参数
    @marshal_with(BookResponseSchema, code=200)  # @marshal_with用于序列化返回结果
    @token_required()
    def put(self, book_id: int, **kwargs):  # 功能：更新书籍信息
        try:
            name = kwargs.get('name')
            author = kwargs.get('author')
            publish_time = kwargs.get('publish_time', None)

            book_model = BookModel(id=book_id, name=name, author=author, publish_time=publish_time)
            book_model = BookService().update_book(book_model)

            return book_model, 200
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
