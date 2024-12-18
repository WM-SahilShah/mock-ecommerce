from app.database import get_db
from app.security import check_admin_role
from app.services.products import ProductService
from app.schemas.products import ProductCreate, ProductOut, ProductsOut, ProductOutDelete, ProductUpdate
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

router = APIRouter(tags=["Products"], prefix="/products")

@router.get("/", status_code=status.HTTP_200_OK, response_model=ProductsOut)
def get_all_products(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number"),
        limit: int = Query(10, ge=1, le=100, description="Items per page"),
        search: str | None = Query("", description="Search based title of products"),
    ) -> ProductsOut:
    "Retrieve all products with pagination and optional search by title."
    return ProductService.get_all_products(db, page, limit, search)

@router.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def get_product(
        product_id: int,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Retrieve a specific product by its ID."
    return ProductService.get_product(db, product_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut, dependencies=[Depends(check_admin_role)])
def create_product(
        product: ProductCreate,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Create a new product."
    return ProductService.create_product(db, product)

@router.put("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut, dependencies=[Depends(check_admin_role)])
def update_product(
        product_id: int,
        updated_product: ProductUpdate,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Update an existing product by its ID."
    return ProductService.update_product(db, product_id, updated_product)


# Delete Product By ID
@router.delete("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOutDelete, dependencies=[Depends(check_admin_role)])
def delete_product(
        product_id: int,
        db: Session = Depends(get_db)
    ) -> ProductOutDelete:
    "Delete a product by its ID."
    return ProductService.delete_product(db, product_id)
