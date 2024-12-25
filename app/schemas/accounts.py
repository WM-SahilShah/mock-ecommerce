from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List

class AccountBase(BaseModel):
    "Schema for basic account details."
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    class Config:
        from_attributes = True

class AccountUpdate(BaseModel):
    "Schema for updating account details."
    username: str
    email: EmailStr
    full_name: str

class AccountOut(BaseModel):
    "Schema for account output with a message and account data."
    message: str
    data: AccountBase

    class Config:
        from_attributes = True
