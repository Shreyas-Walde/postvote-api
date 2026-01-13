from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI() # instace of fastapi with function

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#   get -> http method to read
@app.get("/")
def root():
    return {"message": "Hello World pushing"}

# example database 

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i 

# # for test
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
    
#     posts = db.query(models.Post).all()  # every single entry in post table
#     return {"data": posts}



