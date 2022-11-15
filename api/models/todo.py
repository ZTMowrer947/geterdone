from datetime import datetime
from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    description: str = ""
    start_date: datetime = datetime.today()
    completed: bool = False
