from typing import Union
from fastapi import FastAPI
from app.api.v1.routers import user, auth
from .db.database import get_db
from fastapi import Depends
from .db.database import SessionLocal
from .config.middleware import setup_middleware


app = FastAPI()

setup_middleware(app)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Message": "Welcome to Mirror Feed"}
# @app.get("/")
# def read_root(db: SessionLocal = Depends(get_db)):
#     # Your database operations here
#     return {"message": "Hello, database connected!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}




