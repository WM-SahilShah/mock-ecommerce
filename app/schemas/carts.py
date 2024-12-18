from app.schemas.products import CategoryBase, ProductBase
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

class BaseConfig:
    "Base configuration for Pydantic models."
    from_attributes = True

class ProductBaseCart(ProductBase):
    "Schema for product details within a cart."
    category: CategoryBase = Field(exclude=True)

    class Config(BaseConfig):
        pass

class CartItemBase(BaseModel):
    "Schema for a cart item."
    id: int
    product_id: int
    quantity: int
    subtotal: float
    product: ProductBaseCart

class CartBase(BaseModel):
    "Schema for basic cart details."
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass

class CartOutBase(BaseModel):
    "Schema for cart details output."
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass

class CartOut(BaseModel):
    "Schema for a single cart response."
    message: str
    data: CartBase

    class Config(BaseConfig):
        pass

class CartsOutList(BaseModel):
    "Schema for a list of carts response."
    message: str
    data: List[CartBase]

class CartsUserOutList(BaseModel):
    "Schema for a list of user carts response."
    message: str
    data: List[CartBase]

    class Config(BaseConfig):
        pass

class CartOutDelete(BaseModel):
    "Schema for cart deletion response."
    message: str
    data: CartOutBase

class CartItemCreate(BaseModel):
    "Schema for creating a cart item."
    product_id: int
    quantity: int

class CartCreate(BaseModel):
    "Schema for creating a cart."
    cart_items: List[CartItemCreate]

    class Config(BaseConfig):
        pass

class CartUpdate(CartCreate):
    "Schema for updating a cart."
    pass
