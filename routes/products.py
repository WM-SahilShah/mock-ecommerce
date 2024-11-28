from fastapi import APIRouter, HTTPException, Depends, status, Request
from typing import List
from pydantic import BaseModel
import json

router = APIRouter()

API_KEY = "test_api_key"

class Rating(BaseModel):
    user_id: int
    stars: int

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    ratings: List[Rating]

try:
    with open("data/products.json") as f:
        products = [Product(**prod) for prod in json.load(f)]
except (FileNotFoundError, json.JSONDecodeError) as e:
    products = []
    print(f"Error loading products: {e}")

def api_key_auth(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get("/", response_model=List[Product])
async def get_all_products(api_key: str = Depends(api_key_auth)):
    return products

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int, api_key: str = Depends(api_key_auth)):
    product = next((prod for prod in products if prod.product_id == product_id), None)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
