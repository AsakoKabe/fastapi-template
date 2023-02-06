from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr, validator

from app.config import get_settings


class RegistrationForm(BaseModel):
    username: str
    # password: constr(min_length=8)
    password: str
    email: EmailStr | None

    @validator("password")
    def validate_password(cls, password):
        if not password:
            raise HTTPException(
                status_code=400,
                detail="Password must not be empty string"
            )
        settings = get_settings()
        password = settings.PWD_CONTEXT.hash(password)
        return password

    @validator("username")
    def validate_username(cls, username):
        if not username:
            raise HTTPException(
                status_code=400,
                detail='Username must not be empty string'
            )

        return username


class RegistrationSuccess(BaseModel):
    message: str