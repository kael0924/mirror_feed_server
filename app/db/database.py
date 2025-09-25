from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .dbconf import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        print("Attempting to connect to the database...")
        print("Database connection established.")
        yield db
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise # Re-raise the exception to propagate the error
    finally:
        print("Database closing.")
        db.close()


