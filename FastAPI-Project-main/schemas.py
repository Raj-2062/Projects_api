from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class AccommodationName(str, Enum):
    hotel = "hotel"
    dorm = "dorm"


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class VerifyCode(BaseModel):
    email: EmailStr
    code: str

class UserUpdate(BaseModel):
    full_name: Optional[str]
    age: Optional[int]

class HotelCreate(BaseModel):
    name: str
    location: str

class DormCreate(BaseModel):
    name: str
    location: str

class UserUpdate(BaseModel):
    full_name: str | None = None
    age: int | None = None

class AccommodationName(str,Enum):
    permanent = "permanent"
    temporary = "temporary"