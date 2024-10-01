from fastapi import APIRouter
from src.database import SessionLocal

import src.screenings.utils as utils
from src.screenings.schemas import ScreeningInput, ScreeningBase, ScreeningWithMovieInfo

router = APIRouter(prefix="/screenings", tags=["screenings"])


@router.get('/', response_model=list[ScreeningWithMovieInfo])
async def get_screenings():
    with SessionLocal() as session:
        screenings_with_movie_info = utils.get_all_screenings(session)
    return screenings_with_movie_info


@router.post('/', response_model=ScreeningWithMovieInfo)
async def create_screening(screening: ScreeningInput):
    with SessionLocal() as session:
        session.expire_on_commit = False
        new_screening = utils.create_screening(session, screening)
    return new_screening


@router.put('/{screening_id}', response_model=ScreeningWithMovieInfo)
async def update_screening(screening_id: int, screening: ScreeningInput):
    with SessionLocal() as session:
        session.expire_on_commit = False
        new_screening = utils.update_screening(session, screening, screening_id)
    return new_screening


@router.delete('/{screening_id}', response_model=ScreeningWithMovieInfo)
async def delete_screening(screening_id: int):
    with SessionLocal() as session:
        session.expire_on_commit = False
        screening = utils.delete_screening_by_id(session, screening_id)
    return screening

