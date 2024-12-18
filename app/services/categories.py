from app.models import Category
from app.responses import ResponseHandler
from app.schemas.categories import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session

class CategoryService:
    "Service for category-related actions."

    @staticmethod
    def get_all_categories(db: Session, page: int, limit: int, search: str = "") -> dict:
        "Get all categories."
        categories = db.query(Category).order_by(Category.id.asc()).filter(
            Category.name.contains(search)).limit(limit).offset((page - 1) * limit).all()
        return {"message": f"Page {page} with {limit} categories", "data": categories}

    @staticmethod
    def get_category(db: Session, category_id: int) -> dict:
        "Get a category by ID."
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            ResponseHandler.not_found_error("Category", category_id)
        return ResponseHandler.get_single_success(category.name, category_id, category)

    @staticmethod
    def create_category(db: Session, category: CategoryCreate) -> dict:
        "Create a new category."
        category_dict = category.dict()
        db_category = Category(**category_dict)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return ResponseHandler.create_success(db_category.name, db_category.id, db_category)

    @staticmethod
    def update_category(db: Session, category_id: int, updated_category: CategoryUpdate) -> dict:
        "Update a category."
        db_category = db.query(Category).filter(Category.id == category_id).first()
        if not db_category:
            ResponseHandler.not_found_error("Category", category_id)
        for key, value in updated_category.model_dump().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
        return ResponseHandler.update_success(db_category.name, db_category.id, db_category)

    @staticmethod
    def delete_category(db: Session, category_id: int) -> dict:
        "Delete a category."
        db_category = db.query(Category).filter(Category.id == category_id).first()
        if not db_category:
            ResponseHandler.not_found_error("Category", category_id)
        db.delete(db_category)
        db.commit()
        return ResponseHandler.delete_success(db_category.name, db_category.id, db_category)
