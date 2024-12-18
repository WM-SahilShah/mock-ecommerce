from app.schemas.categories import CategoryBase
from datetime import datetime
from typing import ClassVar, List, Optional
from pydantic import BaseModel, validator

class BaseConfig:
    "Base configuration for Pydantic models."
    from_attributes = True

class ProductBase(BaseModel):
    "Schema for basic product details."
    id: int
    title: str
    description: Optional[str]
    price: int
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime
    category_id: int
    category: CategoryBase

    @validator("discount_percentage", pre=True)
    def validate_discount_percentage(cls, v):
        "Ensure discount percentage is between 0 and 100."
        if v < 0 or v > 100:
            raise ValueError("discount_percentage must be between 0 and 100")
        return v

    class Config(BaseConfig):
        pass

class ProductCreate(ProductBase):
    "Schema for creating a product."
    id: ClassVar[int]
    category: ClassVar[CategoryBase]

    class Config(BaseConfig):
        pass

class ProductUpdate(ProductCreate):
    "Schema for updating a product."
    pass

class ProductOut(BaseModel):
    "Schema for single product output."
    message: str
    data: ProductBase

    class Config(BaseConfig):
        pass

class ProductsOut(BaseModel):
    "Schema for multiple products output."
    message: str
    data: List[ProductBase]

    class Config(BaseConfig):
        pass

class ProductDelete(ProductBase):
    "Schema for deleted product details."
    category: ClassVar[CategoryBase]

class ProductOutDelete(BaseModel):
    "Schema for product deletion output."
    message: str
    data: ProductDelete
