from functools import wraps
from flask import request
from common.constants import LOGIN_SECRET
import jwt


def token_required():
    def check_token(f):
        @wraps(f)
        def wrapper(*arges, **kwargs):
            jwt_token = request.headers.get(key='token', default=None)  # 提取头部token
            if not jwt_token:  # 判断token是否存在
                return {'error': 'Please provide token'}, 401
            try:
                user_info = jwt.decode(jwt_token, LOGIN_SECRET, algorithms=['HS256'])  # 解析token
                if not user_info or not user_info.get('username', None):  # 判断token是否有效
                    return {'error': 'Please provide valid token'}, 401
            except Exception as error:
                return {'error': 'User unauthorized'}, 401

            result = f(*arges, **kwargs)
            return result

        return wrapper

    return check_token
