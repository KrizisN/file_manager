from typing import List, Any
from sqlalchemy import create_engine

from config import Config
from file_manager_app import db


class DBConnection:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.connection = self.engine.connect()

    def select(self, select_statement):
        return self.connection.execute(select_statement)


def safe_bulk_insert(data: List[Any]):
    db.session.bulk_save_objects(data)
    db.session.commit()


db_connection = DBConnection()
