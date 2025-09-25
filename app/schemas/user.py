from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str 
    email: EmailStr
    password: str

class UserCreate(UserBase):
    first_name: str 
    middle_name: Optional[str] = None 
    last_name: str 
    contact_number: Optional[str] = Field(None, pattern=r"^\d{11}$")

class UserLogin(BaseModel):
    username: str    
    password: str 

class UserLogout(BaseModel):
    username: str 
    email: str

class UserOutput(BaseModel):
    id: int
    username: str 
    email: EmailStr
    first_name: str
    middle_name: Optional[str] = None 
    last_name: str 
    is_active: bool 
    is_online: bool 
    created_at: datetime 
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) # crucial


    
