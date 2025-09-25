from typing import Union
from fastapi import FastAPI

from .db.database import get_db
from fastapi import Depends
from .db.database import SessionLocal
import os


app = FastAPI()

# @app.get("/")
# def read_root(db: SessionLocal = Depends(get_db)):
#     # Your database operations here
#     return {"message": "Hello, database connected!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

db_url = os.getenv('DATABASE_URL')
print(f"Database URL: {db_url}")

