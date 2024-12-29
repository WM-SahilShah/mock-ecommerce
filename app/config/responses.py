from fastapi import HTTPException, status
from typing import Optional, Any

class NEstr(str):
    "Non-Empty string type"
    def __new__(cls, value: str) -> "NEstr":
        if not value:
            raise ValueError("String cannot be empty")
        return super().__new__(cls, value)


class ResponseHandler:
    @staticmethod
    def success(message: str, data: Optional[Any] = None) -> dict:
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
    def not_found_error(name: str = "", id: Optional[int] = None) -> None:
        "Raises a 404 error when a resource is not found."
        message = f"{name} With Id {id} Not Found!"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    @staticmethod
    def invalid_token(name: str = "") -> None:
        "Raises a 401 error when a token is invalid."
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid {name} token.",
            headers={"WWW-Authenticate": "Bearer"})
