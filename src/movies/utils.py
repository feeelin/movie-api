from sqlalchemy.orm import Session

from src.movies.models import Movie
import src.movies.schemas as schemas


def get_all_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()


def get_movie_by_id(db: Session, movie_id: int) -> Movie:
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(db: Session, movie: schemas.MovieBase) -> Movie:
    movie = Movie(
        title=movie.title,
        director=movie.director,
        duration=movie.duration,
        start=movie.start,
        end=movie.end
    )
    db.add(movie)
    db.commit()
    return movie


def update_movie(db: Session, new_movie: Movie, movie_id: int) -> Movie:
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    movie.title = new_movie.title
    movie.director = new_movie.director
    movie.duration = new_movie.duration
    movie.start = new_movie.start
    movie.end = new_movie.end

    db.add(movie)
    db.commit()

    return movie


def delete_movie_by_id(db: Session, movie_id: int) -> Movie:
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.delete(movie)
    db.commit()
    return movie
