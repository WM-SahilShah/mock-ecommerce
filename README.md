# Mock E-Commerce Server

This is a mock e-commerce API built with FastAPI. It supports fetching product information with authorization using an API key.

## Features
- **GET /products**: Fetch all products.
- **GET /products/{product_id}**: Fetch details of a specific product.
- **API Key**: Username and password required for all endpoints.

## Setup
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd mock_ecommerce
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:8000`.

4. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Authentication
All API endpoints require an **API Key**. Use the following credentials:
- **Header Name**: "x-api-key"
- **API Key**: "test_api_key"

### Example Request (GET `/products`):
```bash
curl -H "x-api-key: test_api_key" http://127.0.0.1:8000/products
```

### Example Request (GET `/products/{product_id}`):
```bash
curl -H "x-api-key: test_api_key" http://127.0.0.1:8000/products/1
```

## API Endpoints

### GET `/products/`
Retrieve a list of all products.  
**Response**: A JSON array containing all the products.

### GET `/products/{product_id}`
Retrieve details of a specific product by its ID.  
**Response**: A JSON object representing the product details.

---

Feel free to modify the `products.json` file for updates to the product list. The product data is static and can be edited manually from the backend.
