from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # 实例化Flask对象
api = Api(app)          # 实例化Api对象
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/restful_db'  # 配置数据库连接
db = SQLAlchemy(app)    # 实例化SQLAlchemy对象

from resources import student_resources  # 导入student_resources模块中的所有内容
from resources import book_resource      # 导入book_resource模块中的所有内容
from resources import user_resources     # 导入user_resources模块中的所有内容
