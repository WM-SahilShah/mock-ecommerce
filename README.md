# Mock E-Commerce API

A simple Ecommerce API built with Fast API Framework

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Resources](#resources)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)


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
| ReDoc UI | - | `/redoc/` | ReDoc UI for API documentation | - |
| Swagger UI | - | `/docs/` | Swagger UI for API documentation | - |
| Swagger JSON (no UI) | - | `/openapi.json` | OpenAPI JSON for API documentation without UI | - |
| User Signup | POST | `/auth/signup/` | Register a new user | - |
| User Login | POST | `/auth/login/` | Authenticate and generate access tokens for a user | - |
| Refresh Access Token # | POST | `/auth/refresh/` | Refresh an access token using a refresh token | User/Admin |
| Get My Info # | GET | `/me/` | Get information about the authenticated user | User |
| Edit My Info # | PUT | `/me/` | Edit the information of the authenticated user | User |
| Delete My Info # | DELETE | `/me/` | Remove the account of the authenticated user | User |
| Get All Categories | GET | `/categories/` | Get a list of all categories | - |
| Create New Category ## | POST | `/categories/` | Create a new category | Admin |
| Get Specific Category | GET | `/categories/{category_id}/` | Get details of a specific category by ID | - |
| Update Existing Category ## | PUT | `/categories/{category_id}/` | Update details of a specific category by ID | Admin |
| Delete Existing Category ## | DELETE | `/categories/{category_id}/` | Delete a specific category by ID | Admin |
| Get All Products | GET | `/products/` | Get a list of all products | - |
| Create New Product ## | POST | `/products/` | Create a new product | Admin |
| Get Specific Product | GET | `/products/{product_id}/` | Get details of a specific product by ID | - |
| Update Existing Product ## | PUT | `/products/{product_id}/` | Update details of a specific product by ID | Admin |
| Delete Existing Product ## | DELETE | `/products/{product_id}/` | Delete a specific product by ID | Admin |
| Get All Carts # | GET | `/carts/` | Get a list of all carts made by the user | User |
| Create New Cart # | POST | `/carts/` | Create a new cart for the user | User |
| Get Specific Cart # | GET | `/carts/{cart_id}/` | Get details of a specific cart by ID | User |
| Update Existing Cart # | PUT | `/carts/{cart_id}/` | Update details of a specific cart by ID | User |
| Delete Existing Cart # | DELETE | `/carts/{cart_id}/` | Delete a specific cart by ID | User |
| Get All Users ## | GET | `/users/` | Get a list of all users | Admin |
| Create New User ## | POST | `/users/` | Create a new user | Admin |
| Get Specific User ## | GET | `/users/{user_id}/` | Get details of a specific user by ID | Admin |
| Update Existing User ## | PUT | `/users/{user_id}/` | Update details of a specific user by ID | Admin |
| Delete Existing User ## | DELETE | `/users/{user_id}/` | Delete a specific user by ID | Admin |
> Note:  \# marks indicate the level of protection: - for calls that don't need any authentication, # for user calls, ## for admin only calls

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WM-SahilShah/mock-ecommerce
   ```

2. **Navigate to the project directory:**
   ```bash
   cd mock-ecommerce
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


## General Usage

- **Signup**
   - To access the resources, you must have a registered username

- **Login**
   - Every session must start with a login to get authenticated (for 30min at a time). You can either log in as a `user` or `admin`.
   - To get the admin credentials, contact the repo owner. There is no way to create a new admin without editing the database directly to maintain security.
   - If you are using the Swagger UI, paste the access token into the green `Authorize` button at the very top so that you don't have to keep doing it for every API call.

- **Play around!**
  - Have fun with the repo and discover API testing!
  - If your authentication runs out, simply hit the `/auth/refresh/` endpoint with the refresh token obtained in your initial login. If you cannot find it, simply log in again.

## Watermelon Training

- **Step 1: Download the resources**
   - Download the `E-Commerce Files.zip` file using the button given below.
   - Unzip it to see 3 JSON files.

- **Step 2: Upload the API**
   - Open your Watermelon environment.
   - Go to the Lightning API module.
   - Press the `X` (Close) button on the bottom left till it takes you to the home page if you're not already there.
   - Press the `▶` (Begin) button. You should see the API Workbench Modal.
   - Click on `Import API Spec` > `Import From File` and then select/drag the file called `E-Commerce PM Collection.json`.
   
- **Step 3: Upload the Environment Variables**
   - Click on the `Environment` tab on the bottom left vertical panel.
   - Click on `My Environment`. Click on the `+` icon under `Create New`.
   - Fill in the Name and Description fields with values of your choice. eg. "Name: Demo Environment", "Description: Variables common for all the API calls."
   - Click the "Save" icon (floppy disk) under the `Description` field. You should be able to see your new environment as a card in the list of your environments.
   - Click on the "Options" icon (3 vertical dots) on the top right corner of your environment card. Click on `Edit`.
   - Select the "Import" icon (down arrow) under the `Description` field. You should get a modal that will accept files. Select/drag the file `E-Commerce Environment.json`.
   - You should see the values populated in your environment under the `Variables` tab. Click the "Save" icon.
   - Click the "Edit" (pencil) button under the `Actions` column to edit the values of any variable. Change the `Current Value` of the following variables to the values given below:
      - `username`: < your name >
      - `password`: < a password of your choice, ideally the same as your username >
   - Click on the "Save" icon again and you're good to start!

- **Step 4: Make your first API call**
   - On the RHS vertical panel, click on the `API` tab.
   - Select the `>` button in the LHS panel on the right of "26" (the number of API calls in the collection). It should open a summary of your collection.
   - In the `Environment` dropdown, select your environment ("Demo Environment") and click "Save" icon on the right of it.
   - Directly under this, unfold the `Auth` folder to click on `USER SIGNUP`.
   - Directly under the URL (top left of the API Screen), you should be able to see a navbar with a value `REQUEST BODY`. Click on it.
   - Make sure you have the `raw` radio button selected and the `Raw Type` dropdown selected to `JSON`.
   - Click the "Edit" (pencil) icon on the right of `REQUEST BODY` to edit your request.
   - Enter valid text credentials to make your account. [!IMPORTANT] the username and password you enter here should exactly match those you entered in your environment.
   - Click on the "Save" icon on the top RHS corner of the API Screen. Click `Execute` once the changes are saved.

- **Step 5: Set-up your Authentication**
   - Click on the `Auth` tab on your RHS vertical panel.
   - Click on  `+` under `Create New`.
   - Give your auth profile a name, like "Demo Auth"
   - In the `AUTH Type` dropdown, scroll down to the bottom and select `From API`. You should be able to see more configurations.
   - In the `Select API` dropdown, select the entry for `User Login`. Watermelon should have populated the following values for you, verify these/edit to match values:
      - `Token Key`: `Authorization`
      - `Token Value`: `access_token`
      - `Token Prefix`: `Bearer`
      - `Add To`: `HEADER`
      - `Time to Live Path`: `expire_in`
   - Click `Save` on the bottom right. You should be able to see your auth profile card in the list of profiles.
   - Click on the "Options" icon on the top right corner of your card. and then select `Set Auth`. Confirm if you can see it selected above `Create New`.

- **Step 6: Verify Set-up**
   - Click on the `API` tab on the RHS vertical panel.
   - On the LHS Panel, you should be able to see a "fingerprint" icon with a red dot and `Not Authenticated` next to it. Click on it to update your access token.
   - Your first attempt may fail if the server was not recently pinged. Simply try once more after 30s. You should see the red dot turn green.
   - In the API List, unfold the `Me` folder and select the `Get My Info` Call.
   - Click `Execute`. If you get your account details back, your set-up was successful. Enjoy!