from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.dbconf import PUBLIC_CLIENT_URL


def setup_middleware(app: FastAPI):
    origins = [
        PUBLIC_CLIENT_URL
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"],
    )

    