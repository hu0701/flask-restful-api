from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger import swagger    # 导入swagger模块版本为0.20 ,项目中flask版本为3.0.0。装 flask_restful_swagger 时，它强制降级了 Flask 到 1.1.4，安装完成把flask1.1.4删除，重新安装flask 3.0.0，否则flask-sqlalchemy、flask-apispec等插件会报错
from apispec import APISpec                             # swagger模块安装完成后，添加这行导入
from apispec.ext.marshmallow import MarshmallowPlugin   # swagger模块安装完成后，添加这行导入

app = Flask(__name__)  # 实例化Flask对象
api = swagger.docs(Api(app), apiVersion='0.1')  # 实例化Api对象,并使用swagger进行文档化 ,apiVersion表示版本号
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/restful_db'  # 配置数据库连接
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask Restful API Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui',
})

db = SQLAlchemy(app)  # 实例化SQLAlchemy对象
docs = FlaskApiSpec(app)  # 实例化FlaskApiSpec对象

from resources import student_resources  # 导入student_resources模块中的所有内容
from resources import book_resource  # 导入book_resource模块中的所有内容
from resources import user_resources  # 导入user_resources模块中的所有内容
from resources import attachment_resouces  # 导入resources模块中的所有内容


