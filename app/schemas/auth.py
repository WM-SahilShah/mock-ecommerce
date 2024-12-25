from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List

class BaseConfig:
    "Base configuration for Pydantic models."
    from_attributes = True

class UserBase(BaseModel):
    "Schema for basic user details."
    id: int
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: str
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    class Config(BaseConfig):
        pass

class Signup(BaseModel):
    "Schema for user signup details."
    full_name: str
    username: str
    email: str
    password: str

    class Config(BaseConfig):
        pass

class UserOut(BaseModel):
    "Schema for user output with a message and user data."
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass

class TokenResponse(BaseModel):
    "Schema for token response."
    access_token: str
    refresh_token: str
    token_type: str = 'Bearer'
    expires_in: int
