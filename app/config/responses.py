from fastapi import HTTPException, status
from typing import Any

class BaseConfig:
    "Base configuration for Pydantic models"
    from_attributes = True


class ResponseHandler:
    @staticmethod
    def success(message: str, data: Any) -> dict:
        "Returns a success response with a message and optional data."
        return {"message": message, "data": data}

    @staticmethod
    def get_single_success(name: str, id: int, data: Any) -> dict:
        "Returns a success response for a single resource with a message and data."
        message = f"Details for {name} with id {id}"
        return ResponseHandler.success(message, data)

    @staticmethod
    def get_all_success(page: int, limit: int, name: str, data: Any) -> dict:
        "Returns a success response for a single resource with a message and data."
        message = f"Page {page} with limit {limit} {name}"
        return ResponseHandler.success(message, data)

    @staticmethod
    def create_success(name: str, id: int, data: Any) -> dict:
        "Returns a success response when a resource is created."
        message = f"{name} with id {id} created successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def update_success(name: str, id: int, data: Any) -> dict:
        "Returns a success response when a resource is updated."
        message = f"{name} with id {id} updated successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def delete_success(name: str, id: int, data: Any) -> dict:
        "Returns a success response when a resource is deleted."
        message = f"{name} with id {id} deleted successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def malformed_request(message: str) -> None:
        "Raises a 400 error."
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=message)

    @staticmethod
    def invalid_credentials(message: str) -> None:
        "Raises a 401 error when a token is invalid."
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            headers={"WWW-Authenticate": "Bearer"},
                            detail=message)

    @staticmethod
    def restricted_access() -> None:
        "Raises a 403 error when the user is not an admin."
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            details="Admin role required")

    @staticmethod
    def not_found_error(item: str) -> None:
        "Raises a 404 error when a resource is not found."
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{item} Not Found!")
