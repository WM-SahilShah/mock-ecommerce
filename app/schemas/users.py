from app.config.responses import NEstr
from app.schemas.carts import CartBase, BaseConfig
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    id: int
    username: NEstr
    email: EmailStr
    full_name: NEstr
    password: NEstr
    role: NEstr
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    class Config(BaseConfig):
        pass

class UserCreate(UserBase):
    id: None
    role: None
    is_active: None
    created_at: None
    carts: None

class UserUpdate(UserCreate):
    email: None

class UserOut(BaseModel):
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass

class UsersOut(BaseModel):
    message: str
    data: List[UserBase]

    class Config(BaseConfig):
        pass

class UserOutDelete(UserOut):
    pass
