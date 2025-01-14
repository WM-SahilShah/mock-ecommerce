from app.config.responses import BaseConfig
from app.schemas.carts import CartBase
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List, Literal

class BaseAttributes(BaseModel):
    "Schema of attributes used in User/Account Base classes."
    id: int = Field(..., description="Unique identifier for the user or account")
    role: Literal["user", "admin"] = Field(..., description="Role of the user (e.g., user or admin)")
    is_active: bool = Field(..., description="Indicates whether the account is active")
    created_at: datetime = Field(..., description="Timestamp when the account was created")
    carts: List[CartBase] = Field(..., description="List of carts associated with the account")

class UpdateAttributes(BaseModel):
    "Schema of attributes used in User/Account Update classes"
    username: str = Field(..., min_length=1)
    full_name: str = Field(..., min_length=1)

class AccountUpdate(UpdateAttributes):
    "Schema for account update."
    email: EmailStr = Field(..., description="Email address of the account holder")

    class Config(BaseConfig):
        pass

class AccountBase(AccountUpdate, BaseAttributes):
    "Schema for account details."
    pass

class AccountOut(BaseModel):
    "Schema for account output"
    "Schema for user details output."
    message: str = Field(..., description="Response message.")
    data: AccountBase = Field(..., description="Account details.")

    class Config(BaseConfig):
        pass