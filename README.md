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

- **Public URL**
   - [mock-ecommerce-zeb2.onrender.com](https://mock-ecommerce-zeb2.onrender.com)

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



| Endpoint | HTTP Method | Path | Description | User Type |
|----------|-------------|------|-------------|-----------|
| ReDoc UI | - | `/redoc/` | ReDoc UI for API documentation | User |
| Swagger UI | - | `/docs/` | Swagger UI for API documentation | User |
| Swagger JSON (no UI) | - | `/openapi.json` | OpenAPI JSON for API documentation without UI | User |
| User Signup | POST | `/auth/signup/` | Register a new user | User |
| User Login | POST | `/auth/login/` | Authenticate and generate access tokens for a user | User |
| Refresh Access Token | POST | `/auth/refresh/` | Refresh an access token using a refresh token | User |
| Get My Account Info | GET | `/me/` | Get information about the authenticated user | User |
| Edit My Account Info | PUT | `/me/` | Edit the information of the authenticated user | User |
| Remove My Account | DELETE | `/me/` | Remove the account of the authenticated user | User |
| Product List | GET | `/products/` | Get a list of all products | User |
| Create Product* | POST | `/products/` | Create a new product | Admin |
| Retrieve Product by ID | GET | `/products/{id}/` | Get details of a specific product by ID | User |
| Update Product by ID* | PUT | `/products/{id}/` | Update details of a specific product by ID | Admin |
| Delete Product by ID* | DELETE | `/products/{id}/` | Delete a specific product by ID | Admin |
| Category List | GET | `/categories/` | Get a list of all categories | User |
| Create Category* | POST | `/categories/` | Create a new category | Admin |
| Retrieve Category by ID | GET | `/categories/{id}/` | Get details of a specific category by ID | User |
| Update Category by ID* | PUT | `/categories/{id}/` | Update details of a specific category by ID | Admin |
| Delete Category by ID* | DELETE | `/categories/{id}/` | Delete a specific category by ID | Admin |
| User List* | GET | `/users/` | Get a list of all users | Admin |
| Create User* | POST | `/users/` | Create a new user | Admin |
| Get User By ID* | GET | `/users/{user_id}/` | Get details of a specific user by ID | Admin |
| Update User By ID* | PUT | `/users/{user_id}/` | Update details of a specific user by ID | Admin |
| Delete User By ID* | DELETE | `/users/{user_id}/` | Delete a specific user by ID | Admin |

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WM-SahilShah/mock-ecommerce
   ```

2. **Navigate to the project directory:**
   ```bash
   cd mock-ecommerce/
   ```

3. **Build the runtime environment:**
   ```bash
   bash build.sh
   ```

5. **Start the server:**
   ```bash
   bash start.sh
   ```

The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Signup**
   - To access the resources, you must have a registered username

- **Login**
   - Every session must start with a login to get authenticated (for 30min at a time). You can either log in as a `user` or `admin`.
   - To get the admin credentials, contact the repo owner. There is no way to create a new admin without editing the database directly to maintain security.
   - If you are using the Swagger UI, paste the access token into the green `Authorize` button at the very top so that you don't have to keep doing it for every API call.

- **Play around!**
  - Have fun with the repo and discover API testing!
  - If your authentication runs out, simply hit the `/auth/refresh/` endpoint with the refresh token obtained in your initial login. If you cannot find it, simply log in again.
