from sqlalchemy.orm import Session

from src.screenings.models import Screening
from src.movies.models import Movie
import src.screenings.schemas as schemas


def get_all_screenings(db: Session) -> list[tuple[Screening, Movie]]:
    data = db.query(Screening, Movie).join(Movie, Screening.movie_id == Movie.id).all()
    return [__make_screening_and_movie_dict(i) for i in data]


def get_screening_by_id(db: Session, screening_id: int) -> dict:
    output = db.query(Screening, Movie).join(Movie, Movie.id == Screening.movie_id).filter(Screening.id == screening_id).first()
    return __make_screening_and_movie_dict(output)


def create_screening(db: Session, new_screening: schemas.Screening) -> Screening:
    screening = Screening(
        time=new_screening.time,
        movie_id=new_screening.movie_id,
        hall=new_screening.hall
    )
    db.add(screening)
    db.commit()

    output = db.query(Screening, Movie).join(Movie, Movie.id == Screening.movie_id).filter(Screening.id == screening.id).first()

    return __make_screening_and_movie_dict(output)


def update_screening(db: Session, new_screening: Screening, screening_id: int) -> dict:
    output = db.query(Screening, Movie).join(Movie, Movie.id == Screening.movie_id).filter(Screening.id == screening_id).first()
    screening = output[0]

    screening.time = new_screening.time
    screening.movie_id = new_screening.movie_id
    screening.hall = new_screening.hall

    db.add(screening)
    db.commit()

    return __make_screening_and_movie_dict(output)


def delete_screening_by_id(db: Session, screening_id: int) -> Screening:
    data = db.query(Screening, Movie).join(Movie, Movie.id == Screening.movie_id).filter(Screening.id == screening_id).first()
    db.delete(data[0])
    db.commit()
    return __make_screening_and_movie_dict(data)


def __make_screening_and_movie_dict(input_data: tuple[Screening, Movie]) -> dict:
    return {
        "screening": input_data[0],
        "movie": input_data[1],
    }
