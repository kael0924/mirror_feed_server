from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 

from app.crud import user as crud_user 
from app.db.database import get_db
from app.schemas.user import UserCreate


router = APIRouter(prefix="/users", tags=["users", "user"])



@router.post('/', response_model=UserCreate, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status=400, detail="Email is already registered")
    
    return crud_user.create_user(db=db, user=user)
