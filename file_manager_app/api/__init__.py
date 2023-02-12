from flask_restful import Api

from .file import FileManager


def register_api(api: Api):
    api.add_resource(FileManager, "/files")
