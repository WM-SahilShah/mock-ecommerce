from app.config.responses import BaseConfig
from app.schemas.accounts import BaseAttributes, UpdateAttributes
from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserUpdate(UpdateAttributes):
    "Schema for updating a user."
    password: str = Field(..., min_length=1, description="Password of the user.")
    
    class Config(BaseConfig):
        pass

class UserCreate(UserUpdate):
    "Schema for creating a user."
    email: EmailStr = Field(..., description="Email address of the user.")

class UserBase(UserCreate, BaseAttributes):
    "Schema for user details."
    pass

class UserOut(BaseModel):
    "Schema for user details output."
    message: str = Field(..., description="Response message.")
    data: UserBase = Field(..., description="User details.")

    class Config(BaseConfig):
        pass

class UsersOut(BaseModel):
    "Schema for multiple user details output."
    message: str = Field(..., description="Response message.")
    data: List[UserBase] = Field(..., description="List of user details.")

    class Config(BaseConfig):
        pass

class UserOutDelete(UserOut):
    "Schema for user delete output."
    pass
