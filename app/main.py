"""
Main entry point for the E-Commerce API. It also provides the API documentation and contact information for support.
Key functionality includes routers for authentication, accounts, products, and more.
Customizes the Swagger UI with syntax highlighting and additional features.
"""

from app.routers import home_router, auth_router, accounts_router, categories_router, products_router, carts_router, users_router
from fastapi import FastAPI

description = """
Welcome to the Mock E-Commerce API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.
Key features include:

- **CRUD**
	- Create, Read, Update, and Delete endpoints.
- **Search**
	- Find specific information with parameters and pagination.
- **Auth**
	- Verify user/admin identity.
	- Secure with Access and Refresh tokens.
- **Permission**
	- Assign roles with specific permissions.
	- Different access levels for User/Admin.
- **Validation**
	- Ensure accurate and secure input data.

For any inquiries, please contact sshah@watermelon.us
"""

app = FastAPI(
    description=description,
    title="E-Commerce API",
    version="2.0.4",
    contact={
        "name": "Sahil Shah",
        "url": "https://github.com/WM-SahilShah",
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)

app.include_router(home_router)
app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(carts_router)
app.include_router(users_router)
