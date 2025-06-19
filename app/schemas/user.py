# /app/schemas/user.py
from pydantic import BaseModel, ConfigDict

# Shared properties
class UserBase(BaseModel):
    username: str

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)