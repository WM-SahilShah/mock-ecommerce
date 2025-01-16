"""
App > Schemas
=============
This module aggregates the schemas used in the application, making them accessible for import in other parts of the app.
Schemas include definitions for accounts, authentication, carts, categories, products, and users.
"""

from .accounts import AccountUpdate, AccountOut
from .auth import TokenResponse, CustomOAuth2PasswordRequestForm
from .carts import CartCreate, CartUpdate, CartOutDelete, CartOut, CartsOut
from .categories import CategoryCreate, CategoryUpdate, CategoryOutDelete, CategoryOut, CategoriesOut
from .products import ProductCreate, ProductUpdate, ProductOutDelete, ProductOut, ProductsOut
from .users import UserCreate, UserUpdate, UserOutDelete, UserOut, UsersOut

__all__ = [
    "AccountUpdate", "AccountOut",
    "TokenResponse", "CustomOAuth2PasswordRequestForm",
    "CartCreate", "CartUpdate", "CartOutDelete", "CartOut", "CartsOut",
    "CategoryCreate", "CategoryUpdate", "CategoryOutDelete", "CategoryOut", "CategoriesOut",
    "ProductCreate", "ProductUpdate", "ProductOutDelete", "ProductOut", "ProductsOut",
    "UserCreate", "UserUpdate", "UserOutDelete", "UserOut", "UsersOut"
]
