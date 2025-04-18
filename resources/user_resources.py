import jwt
from flask import request
from flask_restful import Resource

from common.constants import LOGIN_SECRET
from resources import api

from services.user_service import UserService


class LoginResource(Resource): # 登录资源
    def post(self):
        try:
            request_json = request.json
            if request_json:
                username = request_json.get('username')  # 提取用户名
                password = request_json.get('password')  # 提取密码

                user_model = UserService().login(username, password)  # 调用用户服务进行登录验证
                if user_model:  # 验证对不对
                    user_json = user_model.serialize()  # 调用user_model得到json送出去
                    jwt_token = jwt.encode(user_json, LOGIN_SECRET, algorithm='HS256')  # 生成token
                    user_json['token'] = jwt_token  # 将token添加到json中

                    return user_json, 200  # 返回用户信息
                else:
                    return {'error': 'Username or Password error'}, 401  # 返回错误信息
            else:
                return {'error': 'Please proivde username and password info as a json'}, 400  # 返回错误信息
        except Exception as error:  # 捕获异常
            return {'error': f'{error}'}, 500  # 返回错误信息


api.add_resource(LoginResource, '/login')
