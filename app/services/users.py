from app.models import User
from app.responses import ResponseHandler
from app.schemas.users import UserCreate, UserUpdate
from app.security import get_password_hash
from sqlalchemy.orm import Session

class UserService:
    "Service for user-related actions."

    @staticmethod
    def get_all_users(db: Session, page: int, limit: int, search: str = "", role: str = "user") -> dict:
        "Get all users."
        users = db.query(User).order_by(User.id.asc()).filter(
            User.username.contains(search), User.role == role).limit(limit).offset((page - 1) * limit).all()
        return {"message": f"Page {page} with {limit} users", "data": users}

    @staticmethod
    def get_user(db: Session, user_id: int) -> dict:
        "Get a user by ID."
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            ResponseHandler.not_found_error("User", user_id)
        return ResponseHandler.get_single_success(user.username, user_id, user)

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> dict:
        "Create a new user."
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        db_user = User(id=None, **user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return ResponseHandler.create_success(db_user.username, db_user.id, db_user)

    @staticmethod
    def update_user(db: Session, user_id: int, updated_user: UserUpdate) -> dict:
        "Update a user."
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            ResponseHandler.not_found_error("User", user_id)
        for key, value in updated_user.model_dump().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return ResponseHandler.update_success(db_user.username, db_user.id, db_user)

    @staticmethod
    def delete_user(db: Session, user_id: int) -> dict:
        "Delete a user."
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            ResponseHandler.not_found_error("User", user_id)
        db.delete(db_user)
        db.commit()
        return ResponseHandler.delete_success(db_user.username, db_user.id, db_user)
