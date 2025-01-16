"""
This module defines schemas for user attributes, updates, creation, and outputs.
"""

from .accounts import BaseAttributes, UpdateAttributes
from app.config import BaseConfig
from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserUpdate(UpdateAttributes):
    """
    Represents schema for updating a user.

    Attributes:
    - `username` (str): Username of the user.
    - `full_name` (str): Full name of the user.
    - `password` (str): Password of the user.
    """
    password: str = Field("<string>", min_length=1, description="Password of the user.")

    class Config(BaseConfig):
        pass

class UserCreate(UserUpdate):
    """
    Represents schema for creating a user.

    Attributes:
    - `username` (str): Username of the user.
    - `full_name` (str): Full name of the user.
    - `password` (str): Password of the user.
    - `email` (str): Email address of the user (validated).
    """
    email: EmailStr = Field("email@example.com", description="Email address of the user (validated).")

class UserBase(UserCreate, BaseAttributes):
    """
    Represents detailed schema for a user.

    Attributes:
    - `id` (int): Unique identifier for the user.
    - `role` (str): Role of the user, either 'user' or 'admin'.
    - `is_active` (bool): Indicates whether the user account is active.
    - `created_at` (datetime): Timestamp of user account creation in ISO 8601 format.
    - `carts` (List[CartBase]): List of carts associated with the user.
    - `username` (str): Username of the user.
    - `full_name` (str): Full name of the user.
    - `password` (str): Password of the user.
    - `email` (str): Email address of the user (validated).
    """
    pass

class UserOut(BaseModel):
    """
    Represents the output schema for a single user's details.

    Attributes:
    - `message` (str): Response message.
    - `data` (UserBase): User details, including:
        - `id` (int): Unique identifier for the user.
        - `role` (str): Role of the user, either 'user' or 'admin'.
        - `is_active` (bool): Indicates whether the user account is active.
        - `created_at` (datetime): Timestamp of user account creation in ISO 8601 format.
        - `carts` (List[CartBase]): List of carts associated with the user.
        - `username` (str): Username of the user.
        - `full_name` (str): Full name of the user.
        - `password` (str): Password of the user.
        - `email` (EmailStr): Email address of the user (validated).
    """
    message: str = Field(..., description="Response message.")
    data: UserBase = Field(..., description="User details.")

    class Config(BaseConfig):
        pass

class UsersOut(BaseModel):
    """
    Represents the output schema for multiple users' details.

    Attributes:
    - `message` (str): Response message.
    - `data` (List[UserBase]): List of user details, each including:
        - `id` (int): Unique identifier for the user.
        - `role` (str): Role of the user, either 'user' or 'admin'.
        - `is_active` (bool): Indicates whether the user account is active.
        - `created_at` (datetime): Timestamp of user account creation in ISO 8601 format.
        - `carts` (List[CartBase]): List of carts associated with the user.
        - `username` (str): Username of the user.
        - `full_name` (str): Full name of the user.
        - `password` (str): Password of the user.
        - `email` (EmailStr): Email address of the user (validated).
    """
    message: str = Field(..., description="Response message.")
    data: List[UserBase] = Field(..., description="List of user details.")

    class Config(BaseConfig):
        pass

class UserOutDelete(UserOut):
    """
    Represents the output schema for a user deletion.

    Attributes:
    - `message` (str): Response message.
    - `data` (UserBase): User details, including:
        - `id` (int): Unique identifier for the user.
        - `role` (str): Role of the user, either 'user' or 'admin'.
        - `is_active` (bool): Indicates whether the user account is active.
        - `created_at` (datetime): Timestamp of user account creation in ISO 8601 format.
        - `carts` (List[CartBase]): List of carts associated with the user.
        - `username` (str): Username of the user.
        - `full_name` (str): Full name of the user.
        - `password` (str): Password of the user.
        - `email` (EmailStr): Email address of the user (validated).
    """
    pass
