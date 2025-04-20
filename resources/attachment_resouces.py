from flask import send_file
from flask_restful import reqparse, Resource
from werkzeug.datastructures import FileStorage
from common import utils
from resources import api


class AttachmentListResource(Resource):  # 定义文件上传接口
    def __init__(self):  # 通过初始化方法，定义请求参数
        self.parser = reqparse.RequestParser()  # 使用 reqparse 中RequestParser类，创建一个参数解析器
        self.parser.add_argument("attachment", required=True, type=FileStorage, location="files",
                                 help="Please provide attachment file")
        # 上传文件是key为attachment，类型为FileStorage，必填，位置为files，帮助信息为Please provide attachment file

    def post(self):
        attachment_file = self.parser.parse_args().get("attachment")  # 解析请求参数，获取attachment的文件名
        file_path = utils.get_attachments_path().joinpath(
            attachment_file.filename)  # 保存路径在utils.get_attachments_path()方法中定义，文件名为attachment_file.filename
        attachment_file.save(file_path)  # 保存文件到指定路径

        return {"message": "Upload success"}, 200


class AttachmentDownloadResource(Resource):  # 定义文件下载接口
    def get(self, filename): # 通过get方法，定义请求参数
        file_path = utils.get_attachments_path().joinpath(filename)  # 保存路径在utils.get_attachments_path()方法中定义，文件名为filename
        return send_file(file_path)  # send_file方法用于发送文件


api.add_resource(AttachmentListResource, "/attachments")  # 将AttachmentListResource类添加到api中，路径为/attachments
api.add_resource(AttachmentDownloadResource, "/attachments/<filename>")  # 将AttachmentDownloadResource类添加到api中，路径为/attachments/<filename>
