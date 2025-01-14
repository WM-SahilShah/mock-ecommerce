from pydantic import BaseModel, Field
from typing import List

class CategoryCreate(BaseModel):
    "Schema for basic category details."
    name: str = Field(..., min_length=1, description="Name of the category. Must have at least 1 character.")

class CategoryBase(CategoryCreate):
    "Schema for creating a category."
    id: int = Field(..., description="Unique identifier for the category.")

class CategoryUpdate(CategoryCreate):
    "Schema for updating a category."
    pass

class CategoryOut(BaseModel):
    "Schema for single category output."
    message: str = Field(..., description="Response message.")
    data: CategoryBase = Field(..., description="Details of the category.")

class CategoriesOut(BaseModel):
    "Schema for multiple categories output."
    message: str = Field(..., description="Response message.")
    data: List[CategoryBase] = Field(..., description="List of category details.")

class CategoryDelete(CategoryBase):
    "Schema for deleted category details."
    pass

class CategoryOutDelete(CategoryOut):
    "Schema for category deletion output."
    pass
