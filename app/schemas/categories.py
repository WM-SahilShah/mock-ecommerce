from app.config.responses import BaseConfig
from pydantic import BaseModel, Field
from typing import List

class CategoryCreate(BaseModel):
    "Schema for basic category details."
    name: str = Field(..., min_length=1)

class CategoryBase(CategoryCreate):
    "Schema for creating a category."
    id: int

class CategoryUpdate(CategoryCreate):
    "Schema for updating a category."
    pass

class CategoryOut(BaseModel):
    "Schema for single category output."
    message: str
    data: CategoryBase

class CategoriesOut(BaseModel):
    "Schema for multiple categories output."
    message: str
    data: List[CategoryBase]

class CategoryDelete(CategoryBase):
    "Schema for deleted category details."
    pass

class CategoryOutDelete(CategoryOut):
    "Schema for category deletion output."
    pass
