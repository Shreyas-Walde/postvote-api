from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Annotated
from pydantic import Field
from pydantic.types import conint

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

class PostOut(BaseModel):
    Post: Post
    votes: int


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

class Vote(BaseModel):
    post_id: int 
    dir: Annotated[int, Field(le=1, ge=0)] #le -> less than equal to 
 