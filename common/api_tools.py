# @Description: API工具,创建token验证工具的装饰器

from functools import wraps
from flask import request
from common.constants import LOGIN_SECRET
import jwt


def token_required():  # 创建方法装饰器
    def check_token(f):  # 创建装饰器
        @wraps(f)  # 装饰器装饰器
        def wrapper(*arges, **kwargs):  # 定义装饰器函数，*arges, **kwargs表示接受任意参数
            jwt_token = request.headers.get(key='token', default=None)  # 提取头部token
            if not jwt_token:  # 判断token是否存在
                return {'error': 'Please provide token'}, 401
            try:
                user_info = jwt.decode(jwt_token, LOGIN_SECRET, algorithms=['HS256'])  # 解析token
                if not user_info or not user_info.get('username', None):  # 判断token是否有效
                    return {'error': 'Please provide valid token'}, 401
            except Exception as error:
                return {'error': 'User unauthorized'}, 401

            result = f(*arges, **kwargs)        # result用处：调用被装饰的函数，这里的解释：arges, kwargs表示调用被装饰的函数时传入的参数
            return result   # 返回被装饰的函数的返回值

        return wrapper # 返回装饰器函数

    return check_token # 返回装饰器
