from src.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=False)
    duration = Column(Integer)
    start = Column(DateTime)
    end = Column(DateTime)
