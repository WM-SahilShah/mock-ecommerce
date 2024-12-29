from app.config.responses import BaseConfig
from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserBase(BaseModel):
    id: int
    username: str = Field(..., min_length=1)
    email: EmailStr
    full_name: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)
    role: str = Field(..., min_length=1)
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
