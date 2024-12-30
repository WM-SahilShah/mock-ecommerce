from app.config.logging import logger
from app.config.responses import ResponseHandler
from app.config.security import get_password_hash
from app.database.models import User
from app.schemas.users import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class UserService:
    "Service for user-related actions."

    @staticmethod
    def get_all_users(db: Session, page: int, limit: int, search: str = "", role: str = "user") -> dict:
        "Get all users."
        logger.info(f"Fetching all users with search term '{search}', role '{role}', page {page}, and limit {limit}.")
        users = (db.query(User)
                 .order_by(User.id.asc())
                 .filter(User.username.contains(search),
                         User.role == role)
                 .limit(limit)
                 .offset((page-1) * limit)
                 .all())
        logger.info(f"Successfully retrieved {len(users)} users.")
        return ResponseHandler.get_all_success(page, limit, "users", users)

    @staticmethod
    def get_user(db: Session, user_id: int) -> dict:
        "Get a user by ID."
        logger.info(f"Fetching user with ID {user_id}.")
        user = (db.query(User)
                .filter(User.id == user_id)
                .first())
        if not user:
            logger.error(f"User with ID {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)
        logger.info(f"Successfully retrieved user: {user.username} (ID: {user.id}).")
        return ResponseHandler.get_single_success(user.username, user_id, user)

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> dict:
        "Create a new user."
        logger.info(f"Creating new user with username '{user.username}'.")
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        max_id = (db.query(User.id)
            .filter(User.id >= 500)
            .order_by(User.id.desc())
            .first())
        new_user_id = max_id.id+1 if max_id else 500
        db_user = User(id=new_user_id, **user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Successfully created user: {db_user.username} (ID: {db_user.id}).")
        return ResponseHandler.create_success(db_user.username, db_user.id, db_user)

    @staticmethod
    def update_user(db: Session, user_id: int, updated_user: UserUpdate) -> dict:
        "Update a user."
        logger.info(f"Updating user with ID {user_id}.")
        db_user = (db.query(User)
                   .filter(User.id == user_id)
                   .first())
        if not db_user:
            logger.error(f"User with ID {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)
        for key, value in updated_user.model_dump().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Successfully updated user: {db_user.username} (ID: {db_user.id}).")
        return ResponseHandler.update_success(db_user.username, db_user.id, db_user)

    @staticmethod
    def delete_user(db: Session, user_id: int) -> dict:
        "Delete a user."
        logger.info(f"Deleting user with ID {user_id}.")
        db_user = (db.query(User)
                   .filter(User.id == user_id)
                   .first())
        if not db_user:
            logger.error(f"User with ID {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)
        db.delete(db_user)
        db.commit()
        logger.info(f"Successfully deleted user: {db_user.username} (ID: {db_user.id}).")
        return ResponseHandler.delete_success(db_user.username, db_user.id, db_user)
