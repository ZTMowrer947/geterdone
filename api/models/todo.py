from datetime import datetime
from dataclasses import dataclass
from marshmallow import Schema, fields

@dataclass
class Todo:
    id: int
    title: str
    description: str = ""
    start_date: datetime = datetime.today()
    completed: bool = False


class TodoSchema(Schema):
    title = fields.String(required=True)
    description = fields.String()
    start_date = fields.DateTime()
    completed = fields.Boolean()
