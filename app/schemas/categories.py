from typing import List
from pydantic import BaseModel

class CategoryBase(BaseModel):
    "Schema for basic category details."
    id: int
    name: str

class CategoryCreate(BaseModel):
    "Schema for creating a category."
    name: str

class CategoryUpdate(BaseModel):
    "Schema for updating a category."
    name: str

class CategoryOut(BaseModel):
    "Schema for single category output."
    message: str
    data: CategoryBase

class CategoriesOut(BaseModel):
    "Schema for multiple categories output."
    message: str
    data: List[CategoryBase]

class CategoryDelete(BaseModel):
    "Schema for deleted category details."
    id: int
    name: str

class CategoryOutDelete(BaseModel):
    "Schema for category deletion output."
    message: str
    data: CategoryDelete
