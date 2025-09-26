from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL=os.getenv('DATABASE_URL')
PUBLIC_CLIENT_URL=os.getenv('PUBLIC_CLIENT_URL')
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')