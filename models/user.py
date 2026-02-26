from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserSignUp(BaseModel):
    full_name: str
    phone: str = Field(..., pattern=r"^\d{10}$") # Validates Indian 10-digit numbers
    password: str

class UserInDB(UserSignUp):
    hashed_password: str
    