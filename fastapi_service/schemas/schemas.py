from typing import Optional
from uuid import UUID
import uuid

from pydantic import BaseModel, EmailStr
# what can be done with database

class Su(BaseModel):
    user_id:  Optional[UUID] = uuid.uuid4()
    email: EmailStr
    full_name: Optional[str] = None
    is_superuser: bool = False
    hashed_password: Optional[str] = None

class SuCreate(Su):
    user_id: UUID
    email: EmailStr
    password: str
    is_superuser: bool = False

class SuUpdate(Su):
    email: EmailStr
    password: str

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None
    personal_private_key: Optional[str] = None
    personal_public_key: Optional[str] = None
    app_public_key: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

class Code(BaseModel):
    var: Optional[str] = None
# Additional properties to return via API
class User(UserInDBBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None

class License(BaseModel):
    var: Optional[str] = None

