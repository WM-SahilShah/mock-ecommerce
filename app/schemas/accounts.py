from app.config.responses import BaseConfig
from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List

class AccountBase(BaseModel):
    "Schema for basic account details."
    id: int
    username: str = Field(..., min_length=1)
    email: EmailStr
    full_name: str = Field(..., min_length=1)
    role: str = Field(..., min_length=1)
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    class Config(BaseConfig):
        pass

class AccountUpdate(AccountBase):
    "Schema for updating account details."
    id: None
    role: None
    is_active: None
    created_at: None
    carts: None

class AccountOut(BaseModel):
    "Schema for account output with a message and account data."
    message: str
    data: AccountBase

    class Config:
        from_attributes = True
