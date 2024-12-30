from app.config.responses import BaseConfig
from app.schemas.accounts import BaseAttributes, UpdateAttributes
from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserUpdate(UpdateAttributes):
    "Schema for updating a user."
    password: str = Field(...,min_length=1)
    
    class Config(BaseConfig):
        pass

class UserCreate(UserUpdate):
    "Schema for creating a user."
    email: EmailStr

class UserBase(UserCreate, BaseAttributes):
    "Schema fro user details."
    pass

class UserOut(BaseModel):
    "Schema for user details output."
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass

class UsersOut(BaseModel):
    "Schema for multiple user details output."
    message: str
    data: List[UserBase]

    class Config(BaseConfig):
        pass

class UserOutDelete(UserOut):
    "Schema for user delete output."
    pass
