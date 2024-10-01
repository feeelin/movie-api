from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema

from src.movies.schemas import MovieBase
from datetime import datetime


class ScreeningBase(BaseModel):
    time: datetime
    hall: int


class ScreeningInput(ScreeningBase):
    movie_id: int


class Screening(ScreeningInput):
    id: int

    class Config:
        orm_mode = True


class ScreeningWithMovieInfo(BaseModel):
    screening: ScreeningBase
    movie: MovieBase

    class Config:
        orm_mode = True
