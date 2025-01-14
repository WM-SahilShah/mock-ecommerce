"""
App > Routers
=============
This module imports and consolidates all router definitions for the e-commerce API.
Each router corresponds to a specific section of the application, such as authentication, products, users, etc.
Routers: accounts_router, auth_router, carts_router, categories_router, home_router, products_router, users_router
"""

from .home import router as home_router
from .accounts import router as accounts_router
from .auth import router as auth_router
from .categories import router as categories_router
from .products import router as products_router
from .carts import router as carts_router
from .users import router as users_router

__all__ = [
    "home_router",
    "accounts_router",
    "auth_router",
    "categories_router",
    "products_router",
    "carts_router",
    "users_router",
]