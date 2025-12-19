from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # instace of fastapi with function

# define class for (Pydantic) -> validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field for schema
    rating: Optional[int] = None  


# example database

my


@app.get("/")    # decorator and read
#   get -> http method to read
def root():
    return {"message": "Hello Everynya how are yo?"}

@app.get("/posts")
def get_posts():
    return {"data": "Here is your posts"}

@app.post("/posts")  # create data
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "new post"}