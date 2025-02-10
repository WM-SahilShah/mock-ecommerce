"""
This module provides the ProductService class for handling product-related actions, 
including retrieving, creating, updating, and deleting products in the database.
"""

from app.config import logger, ResponseHandler
from app.database import Category, Product
from app.schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session

class ProductService:
    """
    Service class for product-related actions.

    Methods:
        `get_all_products(db, page, limit, search)`: Retrieve a paginated list of products, optionally filtered by a search term.
        `get_product(db, product_id)`: Retrieve a specific product by its ID.
        `create_product(db, product)`: Create a new product with the provided details.
        `update_product(db, product_id, updated_product)`: Update a specific product's details.
        `delete_product(db, product_id)`: Delete a specific product from the database.
    """

    @staticmethod
    def get_all_products(db: Session, page: int, limit: int, search: str) -> dict:
        "Get all products."
        if search == "{{searchQuery}}": search = ""
        logger.info(f"Fetching all products with search term '{search}', page {page}, and limit {limit}.")
        products = (db.query(Product)
                    .order_by(Product.id.asc())
                    .filter(Product.title.contains(search))
                    .limit(limit)
                    .offset((page-1) * limit)
                    .all())
        logger.info(f"Successfully retrieved {len(products)} products.")
        return ResponseHandler.get_all_success(page, limit, "products", products)

    @staticmethod
    def get_product(db: Session, product_id: int) -> dict:
        "Get a product by ID."
        logger.info(f"Fetching product with ID {product_id}.")
        product = (db.query(Product)
                   .filter(Product.id == product_id)
                   .first())
        if not product:
            logger.error(f"Product with ID {product_id} not found.")
            ResponseHandler.not_found_error("Product", product_id)
        logger.info(f"Successfully retrieved product: {product.title} (ID: {product.id}).")
        return ResponseHandler.get_single_success(product.title, product_id, product)

    def create_product(db: Session, product: ProductCreate) -> dict:
        "Create a new product"
        logger.info(f"Creating product with title '{product.title}' and category ID {product.category_id}.")
        # Check for empty values
        for field, value in product.model_dump().items():
            if not value and value!=0:
                logger.error(f"Field '{field}' cannot be empty.")
                raise ResponseHandler.malformed_request(f"Field '{field}' cannot be empty.")
        # Check if category exists
        category_exists = (db.query(Category)
                           .filter(Category.id == product.category_id)
                           .first())
        if not category_exists:
            logger.error(f"Category with ID {product.category_id} not found.")
            ResponseHandler.not_found_error("Category", product.category_id)
        # Find the next unique ID in the 200s
        max_id = (db.query(Product.id)
                  .filter(Product.id >= 200)
                  .order_by(Product.id.desc())
                  .first())
        new_product_id = max_id.id+1 if max_id else 200
        # Insert into db
        db_product = Product(id=new_product_id, **product.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        logger.info(f"Successfully created product: {db_product.title} (ID: {db_product.id}).")
        return ResponseHandler.create_success(db_product.title, db_product.id, db_product)

    @staticmethod
    def update_product(db: Session, product_id: int, updated_product: ProductUpdate) -> dict:
        "Update a product."
        logger.info(f"Updating product with ID {product_id}.")
        db_product = (db.query(Product)
                      .filter(Product.id == product_id)
                      .first())
        if not db_product:
            logger.error(f"Product with ID {product_id} not found.")
            ResponseHandler.not_found_error("Product", product_id)
        
        for key, value in updated_product.model_dump().items():
            setattr(db_product, key, value)
        
        db.commit()
        db.refresh(db_product)
        logger.info(f"Successfully updated product: {db_product.title} (ID: {db_product.id}).")
        return ResponseHandler.update_success(db_product.title, db_product.id, db_product)

    @staticmethod
    def delete_product(db: Session, product_id: int) -> dict:
        "Delete a product."
        logger.info(f"Deleting product with ID {product_id}.")
        db_product = (db.query(Product)
                      .filter(Product.id == product_id)
                      .first())
        if not db_product:
            logger.error(f"Product with ID {product_id} not found.")
            ResponseHandler.not_found_error("Product", product_id)
        
        db.delete(db_product)
        db.commit()
        logger.info(f"Successfully deleted product: {db_product.title} (ID: {db_product.id}).")
        return ResponseHandler.delete_success(db_product.title, db_product.id, db_product)
