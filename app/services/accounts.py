from app.config.logging import logger
from app.config.responses import ResponseHandler
from app.config.security import get_token_payload
from app.database.models import User
from sqlalchemy.orm import Session

class AccountService:
    "Service for account-related actions."

    @staticmethod
    def get_my_info(db: Session, token: str) -> dict:
        "Retrieve user's information."
        logger.info("Retrieving user info.")
        user_id = get_token_payload(token.credentials).get("id")
        user = (db.query(User)
                .filter(User.id == user_id)
                .first())

        if not user:
            logger.error(f"User with id {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)

        logger.info(f"Successfully retrieved info for user {user.username} (ID: {user.id}).")
        return ResponseHandler.get_single_success(user.username, user.id, user)

    @staticmethod
    def edit_my_info(db: Session, token: str, updated_user: User) -> dict:
        "Edit user's information."
        logger.info("Editing user info.")
        user_id = get_token_payload(token.credentials).get("id")
        db_user = (db.query(User)
                   .filter(User.id == user_id)
                   .first())

        if not db_user:
            logger.error(f"User with id {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)

        for key, value in updated_user.model_dump().items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        logger.info(f"Successfully updated info for user {db_user.username} (ID: {db_user.id}).")
        return ResponseHandler.update_success(db_user.username, db_user.id, db_user)

    @staticmethod
    def remove_my_account(db: Session, token: str) -> dict:
        "Remove user's account."
        logger.info("Removing user account.")
        user_id = get_token_payload(token.credentials).get("id")
        db_user = (db.query(User)
                   .filter(User.id == user_id)
                   .first())

        if not db_user:
            logger.error(f"User with id {user_id} not found.")
            ResponseHandler.not_found_error("User", user_id)

        db.delete(db_user)
        db.commit()
        logger.info(f"User account for {db_user.username} (ID: {db_user.id}) has been removed.")
        return ResponseHandler.delete_success(db_user.username, db_user.id, db_user)