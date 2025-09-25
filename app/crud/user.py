from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump()) 
    # The **user.dict() call unpacks the pydantic model into keyword arguments
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()



def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        for key, value in user_update.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        
        db.commit()
        db.refresh(db_user)
        db.commit()
    
    return db_user

def delete_user(db: Session, user_id: int) -> User | None:
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()
    
    return db_user 