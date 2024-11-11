# app/core/exceptions.py

from typing import Any, Optional

from fastapi import HTTPException, status


class APIException(HTTPException):
    """
    Base class for custom API exceptions.
    Subclasses must provide `status_code` and `default_detail`.
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error occurred."
    default_code = "error"

    def __init__(self, detail: Optional[Any] = None, code: Optional[str] = None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        self.detail = {
            "message": detail,
            "code": code,
            "status_code": self.status_code
        }
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self):
        return str(self.detail)


class BookNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Book does not exist."
    default_code = "book_not_found"


class AuthorNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Author does not exist."
    default_code = "author_not_found"


class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User does not exist."
    default_code = "user_not_found"


class UserWithEmailAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "User with this email already exists."
    default_code = "user_email_already_exists"

class BookUsageNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Book usage does not exist."
    default_code = "book_usage_not_found"