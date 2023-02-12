from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class File:
    file_id: int
    file_name: str
    file: bytes
    timestamp: Optional[datetime] = datetime.utcnow()
