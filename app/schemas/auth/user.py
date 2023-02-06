from datetime import datetime

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    username: str
    email: EmailStr | None

    class Config:
        orm_mode = True
