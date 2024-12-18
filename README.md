# Mock E-Commerce API

A simple Ecommerce API built with Fast API Framework

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Resources](#resources)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Resources

> [!IMPORTANT]
> The Render.com free plan may experience a short delay (approximately 1 minute) when starting up. Please be patient for the initial access.

- **Documentation**
	- [Swagger](https://mock-ecommerce-zeb2.onrender.com/docs)
	- [ReDoc](https://mock-ecommerce-zeb2.onrender.com/redoc)

- **Database Diagram**
	- [dbdiagram](https://dbdiagram.io/d/6574832756d8064ca0b3b776)


## Features

- **Product Endpoints:**
	- Comprehensive CRUD operations for managing product details, covering creation, retrieval, updating, and deletion.
- **User Authentication:**
	- Implementation of secure user authentication using JWT (JSON Web Token) for robust access control and identity verification.
- **Cart Management:**
	- Robust operations for managing shopping carts, empowering users to effortlessly add, remove, or update items in their carts.
- **Search and Filter:**
	- Implementation of advanced search and filter functionalities to elevate the product browsing experience, allowing users to find specific information efficiently.
- **Account Management:**
	- User-friendly operations for managing user accounts, enabling users to retrieve, update, or delete their account information.
- **Swagger / FastAPI Integration:**
	- Seamless integration of Swagger UI or ReDoc for comprehensive API documentation. This ensures developers have clear and accessible documentation to understand and utilize the API effectively.


## Technologies Used

- **FastAPI:** 
	- A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **PostgreSQL:** 
	- A powerful open-source relational database management system used for data storage.
- **Supabase:** 
	- Utilizing Supabase for its real-time database capabilities and other features.
- **JWT Authentication:** 
	- Implementing JSON Web Token authentication for secure user authentication.
- **Pydantic:** 
	- A data validation and settings management library for Python, often used with FastAPI.
- **Uvicorn:** 
	- A lightweight ASGI server that serves FastAPI applications. It is used for running FastAPI applications in production.
- **SQLAlchemy:** 
	- An SQL toolkit and Object-Relational Mapping (ORM) library for Python, useful for database interactions.



## API Endpoints



| Endpoint                          | HTTP Method | Path                                      | Description                                             | User Type       |
|-----------------------------------|-------------|-------------------------------------------|---------------------------------------------------------|-----------------|
| Product List                      | GET         | `/products/`                              | Get a list of all products                               | User            |
| Create Product                    | POST        | `/products/`                              | Create a new product                                     | Admin           |
| Retrieve Product by ID            | GET         | `/products/{id}/`                         | Get details of a specific product by ID                  | User            |
| Update Product by ID              | PUT         | `/products/{id}/`                         | Update details of a specific product by ID               | Admin           |
| Delete Product by ID              | DELETE      | `/products/{id}/`                         | Delete a specific product by ID                          | Admin           |
| Category List                     | GET         | `/categories/`                            | Get a list of all categories                             | User            |
| Create Category                   | POST        | `/categories/`                            | Create a new category                                    | Admin           |
| Retrieve Category by ID           | GET         | `/categories/{id}/`                       | Get details of a specific category by ID                 | User            |
| Update Category by ID             | PUT         | `/categories/{id}/`                       | Update details of a specific category by ID              | Admin           |
| Delete Category by ID             | DELETE      | `/categories/{id}/`                       | Delete a specific category by ID                         | Admin           |
| User List (Admin Only)            | GET         | `/users/`                                 | Get a list of all users (admin-only)                     | Admin           |
| Get User By ID (Admin Only)       | GET         | `/users/{user_id}/`                       | Get details of a specific user by ID (admin-only)       | Admin           |
| Create User (Admin Only)          | POST        | `/users/`                                 | Create a new user (admin-only)                           | Admin           |
| Update User By ID (Admin Only)    | PUT         | `/users/{user_id}/`                       | Update details of a specific user by ID (admin-only)    | Admin           |
| Delete User By ID (Admin Only)    | DELETE      | `/users/{user_id}/`                       | Delete a specific user by ID (admin-only)               | Admin           |
| Get My Account Info               | GET         | `/account/`                               | Get information about the authenticated user            | User            |
| Edit My Account Info              | PUT         | `/account/`                               | Edit the information of the authenticated user           | User            |
| Remove My Account                 | DELETE      | `/account/`                               | Remove the account of the authenticated user             | User            |
| User Signup                       | POST        | `/auth/signup/`                           | Register a new user                                      | User            |
| User Login                        | POST        | `/auth/login/`                            | Authenticate and generate access tokens for a user       | User            |
| Refresh Access Token              | POST        | `/auth/refresh/`                          | Refresh an access token using a refresh token             | User            |
| Swagger UI                        | -           | `/docs/`                                  | Swagger UI for API documentation                         | User            |
| Swagger JSON (without UI)         | -           | `/openapi.json`                           | OpenAPI JSON for API documentation without UI           | User            |
| ReDoc UI                          | -           | `/redoc/`                                | ReDoc UI for API documentation                           | User            |

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WM-SahilShah/mock-ecommerce
   ```

2. **Navigate to the project directory:**
   ```bash
   cd mock-ecommerce/
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv env
   ```

4. **Activate the virtual environment:**
   ```bash
   env\Scripts\activate #on Windows
   source env/bin/activate #on macOS and Linux
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run Alembic migrations:**
   ```bash
   python migrate.py
   ```
   This will apply any pending database migrations.

2. **Run the FastAPI development server:**
   ```bash
   python run.py
   ```
   The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)