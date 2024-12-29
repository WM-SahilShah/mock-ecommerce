from app.config.responses import NEstr
from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List

class BaseConfig:
    "Base configuration for Pydantic models."
    from_attributes = True

class AccountBase(BaseModel):
    "Schema for basic account details."
    id: int
    username: NEstr
    email: EmailStr
    full_name: NEstr
    role: NEstr
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
