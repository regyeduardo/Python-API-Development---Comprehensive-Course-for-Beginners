import time  # pylint: disable=missing-module-docstring

# from random import randrange
from typing import Optional
import psycopg2
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models
from .database import engine, get_db

# from fastapi.params import Body

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):  # pylint: disable=missing-class-docstring
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="root",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection database failed", error)
        time.sleep(2)

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite food", "content": "I like pizza", "id": 2},
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return {"data": posts}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(title=post.title, content=post.content, published=post.published) # Not added to the db yet
    db.add(new_post)
    db.commit() # Saving post in db
    db.refresh(new_post) # It's the same of 'RETURNING *'
    return {"data": new_post}


@app.get("/posts/latest")
def get_lastest_post():
    post = my_posts[-1]
    return {"detail": post}


@app.get("/posts/{id}")
def get_post(id: int):
    query = f""" SELECT * FROM posts WHERE id = {id}"""
    cursor.execute(query)
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    query = f"""  DELETE FROM posts WHERE id = {id} RETURNING * """
    cursor.execute(query)
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )
    return {
        "post_detail": deleted_post,
        "status": Response(status_code=status.HTTP_204_NO_CONTENT),
    }


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    query = f""" UPDATE posts SET title = '{post.title}', content = '{post.content}', published = '{post.published}' WHERE id = {id} RETURNING * """
    cursor.execute(query)
    updated_post = cursor.fetchone()

    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )

    conn.commit()
    return {"data": updated_post}
