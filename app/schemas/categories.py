from app.config.responses import NEstr
from pydantic import BaseModel
from typing import List

from app.schemas.accounts import BaseConfig

class CategoryBase(BaseModel):
    "Schema for basic category details."
    id: int
    name: NEstr
    
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
