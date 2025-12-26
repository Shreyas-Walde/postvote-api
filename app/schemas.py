from pydantic import BaseModel, EmailStr
from datetime import datetime

# Users -> DB
# define class for (Pydantic) -> validation
class PostBase(BaseModel): 
    title: str
    content: str
    published: bool = True  # optional field for schema

class PostCreate(PostBase):
    pass


# DB -> Users (Response)
class Post(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True 


# Create User
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Create User output
class UserOut(BaseModel): 
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True 
