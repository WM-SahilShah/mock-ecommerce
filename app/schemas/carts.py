"""
This module defines schemas for carts, cart items, and related operations.
"""

from .products import ProductBase
from app.config import BaseConfig
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class CartItemBase(BaseModel):
    """
    Represents a cart item.

    Attributes:
    - `id` (int): Unique identifier for the cart item.
    - `product_id` (int): Unique identifier for the product.
    - `quantity` (int): Quantity of the product in the cart.
    - `subtotal` (float): Subtotal amount for the cart item.
    - `product` (ProductBase): Details of the product.
    """
    id: int = Field(..., description="Unique identifier for the cart item.")
    product_id: int = Field(..., description="Unique identifier for the product.")
    quantity: int = Field(..., description="Quantity of the product in the cart.")
    subtotal: float = Field(..., description="Subtotal amount for the cart item.")
    product: ProductBase = Field(..., description="Details of the product.")

class CartBase(BaseModel):
    """
    Represents basic cart details.

    Attributes:
    - `id` (int): Unique identifier for the cart.
    - `user_id` (int): Unique identifier for the user.
    - `created_at` (datetime): Timestamp when the cart was created.
    - `total_amount` (float): Total amount for the cart.
    - `cart_items` (List[CartItemBase]): List of items in the cart.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product to add to the cart.
    """
    id: int = Field(..., description="Unique identifier for the cart.")
    user_id: int = Field(..., description="Unique identifier for the user.")
    created_at: datetime = Field(..., description="Timestamp when the cart was created.")
    total_amount: float = Field(..., description="Total amount for the cart.")
    cart_items: List[CartItemBase] = Field(..., description="List of items in the cart.")

    class Config(BaseConfig):
        pass

class CartOut(BaseModel):
    """
    Represents a single cart response.

    Attributes:
    - `message` (str): Response message.
    - `data` (CartBase): Cart details, including:
        - `id` (int): Unique identifier for the cart.
        - `user_id` (int): Unique identifier for the user.
        - `created_at` (datetime): Timestamp when the cart was created.
        - `total_amount` (float): Total amount for the cart.
        - `cart_items` (List[CartItemBase]): List of items in the cart.
    """
    message: str = Field(..., description="Response message.")
    data: CartBase = Field(..., description="Cart details.")

    class Config(BaseConfig):
        pass

class CartsOutList(BaseModel):
    """
    Represents a list of carts response.

    Attributes:
    - `message` (str): Response message.
    - `data` (List[CartBase]): List of cart details, each including:
        - `id` (int): Unique identifier for the cart.
        - `user_id` (int): Unique identifier for the user.
        - `created_at` (datetime): Timestamp when the cart was created.
        - `total_amount` (float): Total amount for the cart.
        - `cart_items` (List[CartItemBase]): List of items in the cart.
    """
    message: str = Field(..., description="Response message.")
    data: List[CartBase] = Field(..., description="List of cart details.")

class CartOutDelete(CartOut):
    """
    Represents the response schema for cart deletion.

    Attributes:
    - `message` (str): Response message.
    - `data` (CartBase): Deleted cart details, including:
        - `id` (int): Unique identifier for the cart.
        - `user_id` (int): Unique identifier for the user.
        - `created_at` (datetime): Timestamp when the cart was created.
        - `total_amount` (float): Total amount for the cart.
        - `cart_items` (List[CartItemBase]): List of items in the cart.
    """
    pass

class CartItemCreate(BaseModel):
    """
    Represents schema for creating a cart item.

    Attributes:
    - `product_id` (int): Unique identifier for the product.
    - `quantity` (int): Quantity of the product to add to the cart.
    """
    product_id: int = Field(..., description="Unique identifier for the product.")
    quantity: int = Field(..., description="Quantity of the product to add to the cart.")

class CartCreate(BaseModel):
    """
    Represents schema for creating a cart.

    Attributes:
    - `cart_items` (List[CartItemCreate]): List of items to add to the cart.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product to add to the cart.
    """
    cart_items: List[CartItemCreate] = Field(..., description="List of items to add to the cart.")

    class Config(BaseConfig):
        pass

class CartUpdate(CartCreate):
    """
    Represents schema for updating a cart.

    Attributes:
    - `cart_items` (List[CartItemCreate]): List of items to update in the cart.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product to add to the cart.
    """
    pass
