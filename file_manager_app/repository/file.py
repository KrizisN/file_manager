from typing import List, Set

from sqlalchemy import select
from functools import lru_cache

from file_manager_app.manager.dataclasses import File
from file_manager_app.models import file as file_models
from file_manager_app.repository import safe_bulk_insert, db_connection


def get_file_by_id(file_id: int):
    select_statement = select(file_models.File).where(file_models.File.id == file_id)
    return db_connection.select(select_statement).first()


def upload_files(files: List[File]):
    file_ids = get_all_ids()
    model_objects = [
        file_models.File(
            id=file.file_id,
            file_name=file.file_name,
            file=file.file,
            timestamp=file.timestamp,
        )
        for file in files
        if int(file.file_id) not in file_ids
    ]
    safe_bulk_insert(model_objects)


@lru_cache(maxsize=32)
def get_all_ids() -> Set[int]:
    select_statement = select(file_models.File.id)
    return {i[0] for i in db_connection.select(select_statement)}
