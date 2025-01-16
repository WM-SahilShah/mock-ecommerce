"""
This module defines schemas for creating, updating, and outputting product details, as well as handling product deletion.
"""

from app.config import BaseConfig
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class ProductBase(BaseModel):
    """
    Represents basic details of a product.

    Attributes:
    - `id` (int): Unique identifier for the product.
    - `title` (str): Title of the product.
    - `description` (str): Description of the product.
    - `price` (int): Price of the product (>= 0).
    - `discount_percentage` (float): Discount percentage (0-100).
    - `rating` (float): Rating of the product (0-5).
    - `stock` (int): Stock count (>= 0).
    - `brand` (str): Brand of the product.
    - `thumbnail` (str): URL of the product thumbnail.
    - `images` (List[str]): List of image URLs for the product.
    - `is_published` (bool): Whether the product is published or not.
    - `created_at` (datetime): Timestamp when the product was created.
    - `category_id` (int): Unique identifier for the product's category.
    """
    id: int = Field("<integer>", ge=200, le=299, description="Unique identifier for the product.")
    title: str = Field("<string>", min_length=1, description="Title of the product.")
    description: str = Field("<string>", min_length=1, description="Description of the product.")
    price: int = Field("<integer>", ge=0, description="Price of the product (>=0).")
    discount_percentage: float = Field('<float>', ge=0, le=100, description="Discount percentage (0-100).")
    rating: float = Field("<float>", ge=0, le=5, description="Rating of the product (0-5).")
    stock: int = Field("<integer>", ge=0, description="Stock count (>=0).")
    brand: str = Field("<string>", min_length=1, description="Brand of the product.")
    thumbnail: str = Field("<url>", min_length=1, description="URL of the product thumbnail.")
    images: List[str] = Field("<url>", min_items=1, description="List of image URLs for the product.")
    is_published: bool = Field("<boolean>", description="Whether the product is published or not.")
    created_at: datetime = Field("<datetime obj/ISO 8601 string>", description="Timestamp when the product was created.")
    category_id: int = Field("<integer>", description="Unique identifier for the product's category.")

    class Config(BaseConfig):
        pass

class ProductCreate(ProductBase):
    """
    Represents the schema for creating a product.

    Attributes:
    - `id` (int): Unique identifier for the product.
    - `title` (str): Title of the product.
    - `description` (str): Description of the product.
    - `price` (int): Price of the product (>= 0).
    - `discount_percentage` (float): Discount percentage (0-100).
    - `rating` (float): Rating of the product (0-5).
    - `stock` (int): Stock count (>= 0).
    - `brand` (str): Brand of the product.
    - `thumbnail` (str): URL of the product thumbnail.
    - `images` (List[str]): List of image URLs for the product.
    - `is_published` (bool): Whether the product is published or not.
    - `created_at` (datetime): Timestamp when the product was created.
    - `category_id` (int): Unique identifier for the product's category.
    """
    pass

    class Config(BaseConfig):
        pass

class ProductUpdate(ProductCreate):
    """
    Represents the schema for updating a product.

    Attributes:
    - `id` (int): Unique identifier for the product.
    - `title` (str): Title of the product.
    - `description` (str): Description of the product.
    - `price` (int): Price of the product (>= 0).
    - `discount_percentage` (float): Discount percentage (0-100).
    - `rating` (float): Rating of the product (0-5).
    - `stock` (int): Stock count (>= 0).
    - `brand` (str): Brand of the product.
    - `thumbnail` (str): URL of the product thumbnail.
    - `images` (List[str]): List of image URLs for the product.
    - `is_published` (bool): Whether the product is published or not.
    - `created_at` (datetime): Timestamp when the product was created.
    - `category_id` (int): Unique identifier for the product's category.
    """
    pass

class ProductOut(BaseModel):
    """
    Represents the output schema for a single product.

    Attributes:
    - `message` (str): Response message.
    - `data` (ProductBase): Details of the product.
        - `id` (int): Unique identifier for the product.
        - `title` (str): Title of the product.
        - `description` (str): Description of the product.
        - `price` (int): Price of the product (>= 0).
        - `discount_percentage` (float): Discount percentage (0-100).
        - `rating` (float): Rating of the product (0-5).
        - `stock` (int): Stock count (>= 0).
        - `brand` (str): Brand of the product.
        - `thumbnail` (str): URL of the product thumbnail.
        - `images` (List[str]): List of image URLs for the product.
        - `is_published` (bool): Whether the product is published or not.
        - `created_at` (datetime): Timestamp when the product was created.
        - `category_id` (int): Unique identifier for the product's category.
    """
    message: str = Field(..., description="Response message.")
    data: ProductBase = Field(..., description="Product details.")

class ProductsOut(BaseModel):
    """
    Represents the output schema for multiple products.

    Attributes:
    - `message` (str): Response message.
    - `data` (List[ProductBase]): List of product details.
        - `id` (int): Unique identifier for the product.
        - `title` (str): Title of the product.
        - `description` (str): Description of the product.
        - `price` (int): Price of the product (>= 0).
        - `discount_percentage` (float): Discount percentage (0-100).
        - `rating` (float): Rating of the product (0-5).
        - `stock` (int): Stock count (>= 0).
        - `brand` (str): Brand of the product.
        - `thumbnail` (str): URL of the product thumbnail.
        - `images` (List[str]): List of image URLs for the product.
        - `is_published` (bool): Whether the product is published or not.
        - `created_at` (datetime): Timestamp when the product was created.
        - `category_id` (int): Unique identifier for the product's category.
    """
    message: str = Field(..., description="Response message.")
    data: List[ProductBase] = Field(..., description="List of product details.")

    class Config(BaseConfig):
        pass

class ProductOutDelete(ProductOut):
    """
    Represents the output schema for product deletion.

    Attributes:
    - `message` (str): Response message.
    - `data` (ProductBase): Details of the deleted product.
        - `id` (int): Unique identifier for the product.
        - `title` (str): Title of the product.
        - `description` (str): Description of the product.
        - `price` (int): Price of the product (>= 0).
        - `discount_percentage` (float): Discount percentage (0-100).
        - `rating` (float): Rating of the product (0-5).
        - `stock` (int): Stock count (>= 0).
        - `brand` (str): Brand of the product.
        - `thumbnail` (str): URL of the product thumbnail.
        - `images` (List[str]): List of image URLs for the product.
        - `is_published` (bool): Whether the product is published or not.
        - `created_at` (datetime): Timestamp when the product was created.
        - `category_id` (int): Unique identifier for the product's category.
    """
    pass
