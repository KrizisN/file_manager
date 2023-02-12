import base64

from flask_restful import Resource
from flask import request, send_file, make_response
from jsonschema import validate
from io import BytesIO

from .schema import file_schema
from file_manager_app.manager import file as file_manager
from file_manager_app.manager import dataclasses as file_dataclasses


class FileManager(Resource):
    def get(self):
        validate(request.args, file_schema.file_manager_get)
        file_data = self._get_file_by_id(int(request.args["id"]))
        return send_file(path_or_file=BytesIO(file_data.file), download_name=file_data.file_name, as_attachment=True)

    def post(self):
        files = request.files
        file_manager.upload_files(files)
        return 200

    def head(self):
        validate(request.args, file_schema.file_manager_head)
        file_data = self._get_file_by_id(int(request.args["id"]))
        response = make_response("")
        response.headers.update(self._build_response(file_data))
        return response

    @staticmethod
    def _get_file_by_id(file_id) -> file_dataclasses.File:
        return file_manager.get_file_by_id(file_id)

    @staticmethod
    def _build_response(item: file_dataclasses.File):
        return {
            "fileId": item.file_id,
            "fileName": base64.b64encode(item.file_name.encode("utf-8")).decode(
                "utf-8"
            ),  # If it is not being decoded correctly,
            # cause the client library you're using doesn't support decoding of base64 encoded text
            "fileCreatedAt": item.timestamp.isoformat(),
        }
