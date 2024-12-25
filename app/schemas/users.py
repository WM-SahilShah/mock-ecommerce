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

class UserCreate(BaseModel):
    "Schema for creating a user."
    full_name: str
    username: str
    email: str
    password: str

    class Config(BaseConfig):
        pass

class UserUpdate(UserCreate):
    "Schema for updating a user."
    pass

class UserOut(BaseModel):
    "Schema for single user output."
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass

class UsersOut(BaseModel):
    "Schema for multiple users output."
    message: str
    data: List[UserBase]

    class Config(BaseConfig):
        pass

class UserOutDelete(BaseModel):
    "Schema for user deletion output."
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass
