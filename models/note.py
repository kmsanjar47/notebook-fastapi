import datetime

from pydantic import BaseModel


class Note(BaseModel):
    title: str
    description: str
    date: int = datetime.datetime.now()

