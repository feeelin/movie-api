from fastapi import APIRouter
from src.database import SessionLocal

import src.movies.utils as utils
from src.movies.schemas import MovieBase, Movie

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get('/', response_model=list[MovieBase])
async def get_movies():
    with SessionLocal() as session:
        movies = utils.get_all_movies(session)
    return movies


@router.post('/', response_model=Movie)
async def create_movie(movie: MovieBase):
    with SessionLocal() as session:
        session.expire_on_commit = False
        movie = utils.create_movie(session, movie)
    return movie


@router.put('/{movie_id}', response_model=Movie)
async def update_movie(movie_id: int, movie: MovieBase):
    with SessionLocal() as session:
        session.expire_on_commit = False
        movie = utils.update_movie(session, movie, movie_id)
    return movie


@router.delete('/{movie_id}', response_model=Movie)
async def delete_movie(movie_id: int):
    with SessionLocal() as session:
        session.expire_on_commit = False
        movie = utils.delete_movie_by_id(session, movie_id)
    return movie

