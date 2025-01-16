"""
This module defines schemas for user and account attributes, updates, and outputs.
"""

from .carts import CartBase
from app.config import BaseConfig
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List, Literal

class BaseAttributes(BaseModel):
    """
    Represents base attributes for a user or account.

    Attributes:
    - `id` (int): Unique identifier for the user or account.
    - `role` (str): Role of the user, either 'user' or 'admin'.
    - `is_active` (bool): Indicates whether the account is active.
    - `created_at` (datetime): Timestamp of account creation  in ISO 8601 format.
    - `carts` (List[CartBase]): List of carts associated with the account.
    """
    id: int = Field("<integer>", description="Unique identifier for the user or account.")
    role: Literal["user", "admin"] = Field("<string = user/admin", description="Role of the user (user or admin).")
    is_active: bool = Field("<boolean>", description="Indicates whether the account is active.")
    created_at: datetime = Field("<datetime obj/ISO 8601 string>", description="Timestamp when the account was created.")
    carts: List[CartBase] = Field(..., description="List of carts associated with the account.")

class UpdateAttributes(BaseModel):
    """
    Represents updatable attributes for a user or account.

    Attributes:
    - `username` (str): Username of the account holder.
    - `full_name` (str): Full name of the account holder.
    """
    username: str = Field("<string>", min_length=1, description="Username of the account holder.")
    full_name: str = Field("<string>", min_length=1, description="Full name of the account holder.")

class AccountUpdate(UpdateAttributes):
    """
    Represents schema for updating an account.

    Attributes:
    - `username` (str): Username of the account holder.
    - `full_name` (str): Full name of the account holder.
    - `email` (str): Email address of the account holder (validated).
    """
    email: EmailStr = Field("email@example.com*", description="Email address of the account holder (validated).")

    class Config(BaseConfig):
        pass

class AccountBase(AccountUpdate, BaseAttributes):
    """
    Represents details of an account.

    Attributes:
    - `id` (int): Unique identifier for the user or account.
    - `role` (str): Role of the user, either 'user' or 'admin'.
    - `is_active` (bool): Indicates whether the account is active.
    - `created_at` (datetime): Timestamp of account creation  in ISO 8601 format.
    - `carts` (List[CartBase]): List of carts associated with the account.
    - `username` (str): Username of the account holder.
    - `full_name` (str): Full name of the account holder.
    - `email` (str): Email address of the account holder (validated).
    """
    pass

class AccountOut(BaseModel):
    """
    Represents the output schema for account responses.

    Attributes:
    - `message` (str): Response message.
    - `data` (AccountBase): Account details, including:
        - `id` (int): Unique identifier for the user or account.
        - `role` (str): Role of the user, either 'user' or 'admin'.
        - `is_active` (bool): Indicates whether the account is active.
        - `created_at` (datetime): Timestamp of account creation in ISO 8601 format.
        - `carts` (List[CartBase]): List of carts associated with the account.
        - `username` (str): Username of the account holder.
        - `full_name` (str): Full name of the account holder.
        - `email` (str): Email address of the account holder (validated).
    """
    message: str = Field(..., description="Response message.")
    data: AccountBase = Field(..., description="Account details.")

    class Config(BaseConfig):
        pass
