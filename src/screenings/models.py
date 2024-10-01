from src.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Screening(Base):
    __tablename__ = "screenings"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    hall = Column(Integer, nullable=False)
