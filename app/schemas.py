from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Users -> DB
# define class for (Pydantic) -> validation
class PostBase(BaseModel): 
    title: str
    content: str
    published: bool = True  # optional field for schema

class PostCreate(PostBase):
    pass

# Create User output
class UserOut(BaseModel): 
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True   # edit for users!


# DB -> Users (Response)
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        from_attributes = True 


# Create User
class UserCreate(BaseModel):
    email: EmailStr
    password: str


         

# Verify User
class UserLogin(BaseModel): 
    email: EmailStr
    password: str

# Access Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None