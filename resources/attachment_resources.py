from flask import send_file
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage

# reqparse 语法分析器
from utils import token_required, get_attachment_path
from exts import api


class AttachmentResource(Resource):
    # 下载文件
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # 请求参数要包含 attachment ， 数据转换成 type类型 存放在location， 如果出错 help提示
        self.parser.add_argument("attachment", required=True, type=FileStorage, location="files",
                                 help="Please provide attachment file")

    def post(self):
        attachment_file = self.parser.parse_args().get('attachment')
        file_path = get_attachment_path().joinpath(attachment_file.filename)
        attachment_file.save(file_path)

        return {'message': 'ok'}


class AttachmentResourceUpload(Resource):
    def get(self, filename):
        file_path = get_attachment_path().joinpath(filename)
        try:
            return send_file(file_path)
        except Exception as error:
            return {"error": 'Upload failed'}


api.add_resource(AttachmentResource, '/attachments')
api.add_resource(AttachmentResourceUpload, '/attachments/<filename>')
