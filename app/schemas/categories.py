from app.config.responses import BaseConfig
from pydantic import BaseModel, Field
from typing import List

class CategoryBase(BaseModel):
    "Schema for basic category details."
    id: int
    name: str = Field(..., min_length=1)
    
    class Config(BaseConfig):
        pass

class CategoryCreate(CategoryBase):
    "Schema for creating a category."
    id: None

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

class CategoryOutDelete(BaseModel):
    "Schema for category deletion output."
    message: str
    data: CategoryDelete
