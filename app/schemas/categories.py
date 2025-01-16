"""
This module defines schemas for creating, updating, and outputting category details, as well as handling category deletion.
"""

from app.config import CustomBaseModel
from pydantic import Field
from typing import List

class CategoryCreate(CustomBaseModel):
    """
    Represents the basic details for creating a category.

    Attributes:
    - `name` (str): Name of the category.
    """
    name: str = Field("<string>", min_length=1, description="Name of the category. Must have at least 1 character.")

class CategoryBase(CategoryCreate):
    """
    Represents the details of a category.

    Attributes:
    - `id` (int): Unique identifier for the category.
    - `name` (str): Name of the category.
    """
    id: int = Field("<integer>", ge=100, le=199, description="Unique identifier for the category.")

class CategoryUpdate(CategoryCreate):
    """
    Represents the schema for updating a category.

    Attributes:
    - `name` (str): Name of the category.
    """
    pass

class CategoryOut(CustomBaseModel):
    """
    Represents the output schema for a single category.

    Attributes:
    - `message` (str): Response message.
    - `data` (CategoryBase): Details of the category.
        - `id` (int): Unique identifier for the category.
        - `name` (str): Name of the category.
    """
    message: str = Field(..., description="Response message.")
    data: CategoryBase = Field(..., description="Details of the category.")

class CategoriesOut(CustomBaseModel):
    """
    Represents the output schema for multiple categories.

    Attributes:
    - `message` (str): Response message.
    - `data` (List[CategoryBase]): List of category details.
        - `id` (int): Unique identifier for the category.
        - `name` (str): Name of the category.
    """
    message: str = Field(..., description="Response message.")
    data: List[CategoryBase] = Field(..., description="List of category details.")

class CategoryOutDelete(CategoryOut):
    """
    Represents the output schema for category deletion.

    Attributes:
    - `message` (str): Response message.
    - `data` (CategoryBase): Details of the deleted category.
        - `id` (int): Unique identifier for the category.
        - `name` (str): Name of the category.
    """
    pass
