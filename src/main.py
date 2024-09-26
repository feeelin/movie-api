from fastapi import FastAPI
from src.movies.router import router as movies_router

app = FastAPI()

app.include_router(movies_router)
