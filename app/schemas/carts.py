from app.config.responses import BaseConfig
from app.schemas.products import CategoryBase, ProductBase
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class ProductBaseCart(ProductBase):
    "Schema for product details within a cart."
    category: CategoryBase = Field(exclude=True, description="Category details of the product (excluded from output).")

class CartItemBase(BaseModel):
    "Schema for a cart item."
    id: int = Field(..., description="Unique identifier for the cart item.")
    product_id: int = Field(..., description="Unique identifier for the product.")
    quantity: int = Field(..., description="Quantity of the product in the cart.")
    subtotal: float = Field(..., description="Subtotal amount for the cart item.")
    product: ProductBaseCart = Field(..., description="Details of the product.")

class CartBase(BaseModel):
    "Schema for basic cart details."
    id: int = Field(..., description="Unique identifier for the cart.")
    user_id: int = Field(..., description="Unique identifier for the user.")
    created_at: datetime = Field(..., description="Timestamp when the cart was created.")
    total_amount: float = Field(..., description="Total amount for the cart.")
    cart_items: List[CartItemBase] = Field(..., description="List of items in the cart.")

    class Config(BaseConfig):
        pass

class CartOutBase(CartBase):
    "Schema for cart details output."
    pass

class CartOut(BaseModel):
    "Schema for a single cart response."
    message: str = Field(..., description="Response message.")
    data: CartBase = Field(..., description="Cart details.")

    class Config(BaseConfig):
        pass

class CartsOutList(BaseModel):
    "Schema for a list of carts response."
    message: str = Field(..., description="Response message.")
    data: List[CartBase] = Field(..., description="List of cart details.")

class CartsUserOutList(CartsOutList):
    "Schema for a list of user carts response."
    pass

    class Config(BaseConfig):
        pass

class CartOutDelete(CartOut):
    "Schema for cart deletion response."
    pass

class CartItemCreate(BaseModel):
    "Schema for creating a cart item."
    product_id: int = Field(..., description="Unique identifier for the product.")
    quantity: int = Field(..., description="Quantity of the product to add to the cart.")

class CartCreate(BaseModel):
    "Schema for creating a cart."
    cart_items: List[CartItemCreate] = Field(..., description="List of items to add to the cart.")

    class Config(BaseConfig):
        pass

class CartUpdate(CartCreate):
    "Schema for updating a cart."
    pass
