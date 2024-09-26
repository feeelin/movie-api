from pydantic import BaseModel
from datetime import datetime


class MovieBase(BaseModel):
    title: str
    director: str
    duration: int | None
    start: datetime | None
    end: datetime | None


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
