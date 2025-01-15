"""
App > Schemas
=============
This module aggregates the schemas used in the application, making them accessible for import in other parts of the app.
Schemas include definitions for accounts, authentication, carts, categories, products, and users.
"""

from .accounts import AccountUpdate, AccountOut
from .auth import TokenResponse
from .carts import CartCreate, CartOut, CartsOutList, CartOutDelete, CartCreate, CartUpdate
from .categories import CategoryCreate, CategoryUpdate, CategoryOut, CategoriesOut, CategoryOutDelete
from .products import ProductCreate, ProductUpdate, ProductOut, ProductsOut, ProductOutDelete
from .users import UserUpdate, UserCreate, UserOut, UsersOut, UserOutDelete

__all__ = [
    "AccountUpdate", "AccountOut",
    "TokenResponse",
    "CartCreate", "CartOut", "CartsOutList", "CartOutDelete", "CartCreate", "CartUpdate",
    "CategoryCreate", "CategoryUpdate", "CategoryOut", "CategoriesOut", "CategoryOutDelete",
    "ProductCreate", "ProductUpdate", "ProductOut", "ProductsOut", "ProductOutDelete",
    "UserUpdate", "UserCreate", "UserOut", "UsersOut", "UserOutDelete"
]
