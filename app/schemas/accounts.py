from app.config.responses import BaseConfig
from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List

class BaseAttributes(BaseModel):
    id: int
    role: str = Field(..., min_length=1)
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

class UpdateAttributes(BaseModel):
    username: str = Field(..., min_length=1)
    full_name: str = Field(..., min_length=1)

class AccountUpdate(UpdateAttributes):
    email: EmailStr

    class Config(BaseConfig):
        pass

class AccountBase(AccountUpdate, BaseAttributes):
    pass