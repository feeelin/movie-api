from fastapi import FastAPI
from src.movies.router import router as movies_router
from src.screenings.router import router as screening_router

app = FastAPI()

app.include_router(movies_router)
app.include_router(screening_router)
