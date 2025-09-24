from typing import Union
from fastapi import FastAPI
from .routers import auth


app = FastAPI()


app.include_router(auth.router)


@app.get("/")
async def root():
    return {
        "Page": "Index Page"
}