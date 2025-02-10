from app.config import logger, ResponseHandler, get_password_hash
from app.database import User
from app.schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class UserService:
    """
    Service class for user-related actions.

    Methods:
        `get_all_users(db, page, limit, search, role)`: Retrieve a paginated list of users, optionally filtered by a search term and role.
        `get_user(db, user_id)`: Retrieve a specific user by their ID.
        `create_user(db, user)`: Create a new user with the provided details.
        `update_user(db, user_id, updated_user)`: Update a specific user's details.
        `delete_user(db, user_id)`: Delete a specific user from the database.
    """


    @staticmethod
    def get_all_users(db: Session, page: int, limit: int, search: str = "", role: str = "") -> dict:
        "Get all users."
        if search == "{{searchQuery}}": search = ""
        logger.info(f"Fetching all users with search term '{search}', role '{role}', page {page}, and limit {limit}.")
        users = (db.query(User)
                 .order_by(User.id.asc())
                 .filter(User.username.contains(search),
                         User.role.contains(role))
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
        if not user.username or not user.password or not user.email:
            logger.error("User creation failed: Missing required fields.")
            raise ResponseHandler.malformed_request("Missing required fields: username, password, and/or email")
        existing_user = (db.query(User)
                         .filter(User.username == user.username)
                         .first())
        if existing_user:
            logger.error(f"User creation failed: Username {user.username} already exists.")
            raise ResponseHandler.malformed_request("User already exists.")
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        # Find the next unique ID in the 500s
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
