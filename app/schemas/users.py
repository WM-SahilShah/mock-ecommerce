from app.config.responses import BaseConfig
from app.schemas.accounts import BaseAttributes, UpdateAttributes
from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserUpdate(UpdateAttributes):
    password: str = Field(...,min_length=1)
    
    class Config(BaseConfig):
        pass

class UserCreate(UserUpdate):
    email: EmailStr

class UserBase(UserCreate, BaseAttributes):
    pass

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
