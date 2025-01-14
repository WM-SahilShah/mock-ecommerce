from app.config.responses import BaseConfig
from app.schemas.categories import CategoryBase
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class ProductBase(BaseModel):
    "Schema for basic product details."
    id: int = Field(..., description="Unique identifier for the product.")
    title: str = Field(..., min_length=1, description="Title of the product.")
    description: str = Field(..., min_length=1, description="Description of the product.")
    price: int = Field(..., ge=0, description="Price of the product (>=0).")
    discount_percentage: float = Field(..., ge=0, le=100, description="Discount percentage (0-100).")
    rating: float = Field(..., ge=0, le=5, description="Rating of the product (0-5).")
    stock: int = Field(..., ge=0, description="Stock count (>=0).")
    brand: str = Field(..., min_length=1, description="Brand of the product.")
    thumbnail: str = Field(..., min_length=1, description="URL of the product thumbnail.")
    images: List[str] = Field(..., min_items=1, description="List of image URLs for the product.")
    is_published: bool = Field(..., description="Whether the product is published or not.")
    created_at: datetime = Field(..., description="Timestamp when the product was created.")
    category_id: int = Field(..., description="Unique identifier for the product's category.")
    category: CategoryBase = Field(..., description="Details of the product's category.")

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
    message: str = Field(..., description="Response message.")
    data: ProductBase = Field(..., description="Product details.")

class ProductsOut(BaseModel):
    "Schema for multiple products output."
    message: str = Field(..., description="Response message.")
    data: List[ProductBase] = Field(..., description="List of product details.")

    class Config(BaseConfig):
        pass

class ProductDelete(ProductBase):
    "Schema for deleted product details."
    pass

class ProductOutDelete(BaseModel):
    "Schema for product deletion output."
    message: str = Field(..., description="Response message.")
    data: ProductDelete = Field(..., description="Deleted product details.")
