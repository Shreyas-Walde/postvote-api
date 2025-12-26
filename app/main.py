from typing import Optional, List
from fastapi import FastAPI, Response,status, HTTPException, Depends
from fastapi.params import Body

from random import randrange

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI() # instace of fastapi with function

while True:

    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='koyo', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)


# example database

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 

@app.get("/")    # decorator and read
#   get -> http method to read
def root():
    return {"message": "Hello Everynya how are yo?"}

# # for test
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
    
#     posts = db.query(models.Post).all()  # every single entry in post table
#     return {"data": posts}


@app.get("/posts", response_model= List[schemas.Post]) # read
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)  # create 
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db)):    # staging changes to db
    
    # cursor.execute("""INSERT INTO posts(title,content,published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))

    # new_post = cursor.fetchone() 

    # conn.commit()  # to save into postgresdb

    # new_post = models.Post(title=post.title, content=post.content, published=post.published)

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@app.get("/posts/{id}", response_model=schemas.Post)  # read single post
def get_posts(id: int,db: Session = Depends(get_db)):  # validate and automatically c 
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found")

    return post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)  # delete
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exist")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", response_model=schemas.Post) # Update post
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exist")
    
    post_query.update(updated_post.dict(),synchronize_session=False)

    db.commit()

    return post_query.first()

# creating user -> on db
@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut) 
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # hash the password - user.password 
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user