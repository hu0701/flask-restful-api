from flask import Flask

app = Flask(__name__)  # 创建一个Flask应用实例

from routes import student_api
# 注解： 导入student_api.py中的所有路由，为什么要这样写？，
# from写在app实例下面，这写有什么作用吗？ 因为，在python中，from语句用于从一个模块中导入指定对象的，而import语句用于导入整个模块。
# 在这个例子中，from routes import student_api语句用于从routes模块中导入student_api对象，这个对象是一个函数，用于处理与学生相关的API请求。
# 这个函数的定义在student_api.py文件中。将这个函数导入到app实例中，可以让Flask应用知道如何处理与
