from app.config.logging import logger
from app.config.responses import ResponseHandler
from app.database.models import Category
from app.schemas.categories import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session

class CategoryService:
    "Service for category-related actions."

    @staticmethod
    def get_all_categories(db: Session, page: int, limit: int, search: str = "") -> dict:
        "Get all categories."
        logger.info(f"Fetching categories for page {page} with limit {limit} and search term '{search}'.")
        categories = (db.query(Category)
                      .order_by(Category.id.asc())
                      .filter(Category.name.contains(search))
                      .limit(limit)
                      .offset((page-1) * limit)
                      .all())
        logger.info(f"Fetched {len(categories)} categories.")
        return ResponseHandler.get_all_success(page, limit, "categories", categories)

    @staticmethod
    def get_category(db: Session, category_id: int) -> dict:
        "Get a category by ID."
        logger.info(f"Fetching category with ID {category_id}.")
        category = (db.query(Category)
                    .filter(Category.id == category_id)
                    .first())
        if not category:
            logger.error(f"Category with ID {category_id} not found.")
            ResponseHandler.not_found_error("Category", category_id)
        logger.info(f"Successfully retrieved category {category.name} (ID: {category.id}).")
        return ResponseHandler.get_single_success(category.name, category_id, category)

    @staticmethod
    def create_category(db: Session, category: CategoryCreate) -> dict:
        "Create a new category."
        logger.info(f"Creating new category with name {category.name}.")
        category_dict = category.model_dump()
        db_category = Category(**category_dict)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        logger.info(f"Successfully created category {db_category.name} (ID: {db_category.id}).")
        return ResponseHandler.create_success(db_category.name, db_category.id, db_category)

    @staticmethod
    def update_category(db: Session, category_id: int, updated_category: CategoryUpdate) -> dict:
        "Update a category."
        logger.info(f"Updating category with ID {category_id}.")
        db_category = (db.query(Category)
                       .filter(Category.id == category_id)
                       .first())
        if not db_category:
            logger.error(f"Category with ID {category_id} not found.")
            ResponseHandler.not_found_error("Category", category_id)
        
        for key, value in updated_category.model_dump().items():
            setattr(db_category, key, value)
        
        db.commit()
        db.refresh(db_category)
        logger.info(f"Successfully updated category {db_category.name} (ID: {db_category.id}).")
        return ResponseHandler.update_success(db_category.name, db_category.id, db_category)

    @staticmethod
    def delete_category(db: Session, category_id: int) -> dict:
        "Delete a category."
        logger.info(f"Deleting category with ID {category_id}.")
        db_category = (db.query(Category)
                       .filter(Category.id == category_id)
                       .first())
        if not db_category:
            logger.error(f"Category with ID {category_id} not found.")
            ResponseHandler.not_found_error("Category", category_id)
        
        db.delete(db_category)
        db.commit()
        logger.info(f"Successfully deleted category {db_category.name} (ID: {db_category.id}).")
        return ResponseHandler.delete_success(db_category.name, db_category.id, db_category)
