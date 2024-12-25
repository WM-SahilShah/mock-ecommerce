from app.routers import products, categories, carts, users, auth, accounts
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
    version="2.0",
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


app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)
