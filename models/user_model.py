from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from resources import db


class UserModel(db.Model): # 创建用户模型
    __tablename__ = 'users' # 表名
    id: Mapped[int] = mapped_column(Integer, primary_key=True) # ID主键 定义了用户模型，包括id、username和password三个字段，其中id是主键，username和password不能为空，并且username是唯一的。
    username: Mapped[str] = mapped_column(String(128), nullable=False, unique=True) # 用户名
    password: Mapped[str] = mapped_column(String(128), nullable=False)  # 密码

    def serialize(self):    #方法，用于将用户模型序列化为字典
        return {            #返回一个字典，包含用户的id和username
            'id': self.id,
            'username': self.username
        }
