from app.config.responses import BaseConfig
from app.schemas.categories import CategoryBase
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class ProductBase(BaseModel):
    "Schema for basic product details."
    id: int
    title: str = Field(..., min_length=1, description="Title of the product")
    description: str = Field(..., min_length=1, description="Description of the product")
    price: int = Field(..., ge=0, description="Price of the product (>=0)")
    discount_percentage: float = Field(..., ge=0, le=100, description="Discount percentage (0-100)")
    rating: float = Field(..., ge=0, le=5, description="Rating of the product (0-5)")
    stock: int = Field(..., ge=0, description="Stock count (>=0)")
    brand: str = Field(..., min_length=1, description="Brand of the product")
    thumbnail: str = Field(..., min_length=1, description="URL of the product thumbnail")
    images: List[str] = Field(..., min_items=1, description="List of image URLs")
    is_published: bool
    created_at: datetime
    category_id: int
    category: CategoryBase

    class Config(BaseConfig):
        pass

class ProductCreate(ProductBase):
    "Schema for creating a product."
    pass

    class Config(BaseConfig):
        pass

class ProductUpdate(ProductCreate):
    "Schema for updating a product."
    pass

class ProductOut(BaseModel):
    "Schema for single product output."
    message: str
    data: ProductBase

class ProductsOut(BaseModel):
    "Schema for multiple products output."
    message: str
    data: List[ProductBase]

    class Config(BaseConfig):
        pass

class ProductDelete(ProductBase):
    "Schema for deleted product details."
    pass

class ProductOutDelete(BaseModel):
    "Schema for product deletion output."
    message: str
    data: ProductDelete
