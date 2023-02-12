from file_manager_app.manager import dataclasses as manager_dataclasses
from file_manager_app.repository import file as file_repo


def get_file_by_id(file_id: int) -> manager_dataclasses.File:
    file_query = file_repo.get_file_by_id(file_id)
    return manager_dataclasses.File(
        file_id=file_query.id,
        file_name=file_query.file_name,
        file=file_query.file,
        timestamp=file_query.timestamp,
    )


def upload_files(files):
    files = [
        manager_dataclasses.File(
            file_id=file_id,
            file_name=file_info.filename,
            file=file_info.stream.read(),
        )
        for file_id, file_info in files.items()
    ]

    file_repo.upload_files(files)
