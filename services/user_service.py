from sqlalchemy import Select

from models.user_model import UserModel
from resources import db


class UserService:
    def login(self, username: str, password: str):
        print(password)
        query = Select(UserModel).where(UserModel.username == username)  # 构建查询语句
        user_model = db.session.scalars(query).first()      # 查询用户
        if user_model and user_model.password == password:  # 如果用户存在且密码正确
            return user_model  # 返回用户
        else:
            return None  # 否则返回None
