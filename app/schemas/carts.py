"""
This module defines schemas for carts, cart items, and related operations.
"""

from .products import ProductBase
from app.config import CustomBaseModel
from datetime import datetime
from pydantic import Field
from typing import List

class CartItemBase(CustomBaseModel):
    """
    Represents a cart item.

    Attributes:
    - `id` (int): Unique identifier for the cart item.
    - `product_id` (int): Unique identifier for the product.
    - `quantity` (int): Quantity of the product in the cart.
    - `subtotal` (float): Subtotal amount for the cart item.
    - `product` (ProductBase): Details of the product.
    """
    id: int = Field("<integer>", description="Unique identifier for the cart item.")
    product_id: int = Field("<integer>", description="Unique identifier for the product.")
    quantity: int = Field("<integer>", description="Quantity of the product in the cart.")
    subtotal: float = Field("<float>", description="Subtotal amount for the cart item.")
    product: ProductBase = Field(..., description="Details of the product.")

class CartBase(CustomBaseModel):
    """
    Represents basic cart details.

    Attributes:
    - `id` (int): Unique identifier for the cart.
    - `user_id` (int): Unique identifier for the user.
    - `created_at` (datetime): Timestamp when the cart was created.
    - `total_amount` (float): Total amount for the cart.
    - `cart_items` (List[CartItemBase]): List of items in the cart.
        - `id` (int): Unique identifier for the cart item.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product in the cart.
        - `subtotal` (float): Subtotal amount for the cart item.
        - `product` (ProductBase): Details of the product.
    """
    id: int = Field("<integer>", ge=300, le=399, description="Unique identifier for the cart.")
    user_id: int = Field("<integer>", ge=500, le=599, description="Unique identifier for the user.")
    created_at: datetime = Field("<datetime obj/ISO 8601 string>", description="Timestamp when the cart was created.")
    total_amount: float = Field("<float>", description="Total amount for the cart.")
    cart_items: List[CartItemBase] = Field(..., description="List of items in the cart.")

class CartOut(CustomBaseModel):
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

class CartsOut(CustomBaseModel):
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

class CartItemCreate(CustomBaseModel):
    """
    Represents schema for creating a cart item.

    Attributes:
    - `product_id` (int): Unique identifier for the product.
    - `quantity` (int): Quantity of the product to add to the cart.
    """
    product_id: int = Field("<integer>", ge=200, le=299, description="Unique identifier for the product.")
    quantity: int = Field("<integer>", gt=0, description="Quantity of the product to add to the cart.")

class CartCreate(CustomBaseModel):
    """
    Represents schema for creating a cart.

    Attributes:
    - `cart_items` (List[CartItemCreate]): List of items to add to the cart.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product to add to the cart.
    """
    cart_items: List[CartItemCreate] = Field(..., description="List of items to add to the cart.")

class CartUpdate(CartCreate):
    """
    Represents schema for updating a cart.

    Attributes:
    - `cart_items` (List[CartItemCreate]): List of items to update in the cart.
        - `product_id` (int): Unique identifier for the product.
        - `quantity` (int): Quantity of the product to add to the cart.
    """
    pass
