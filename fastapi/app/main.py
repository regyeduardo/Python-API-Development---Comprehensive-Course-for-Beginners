import time  # pylint: disable=missing-module-docstring

# from random import randrange
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user

# from fastapi.params import Body

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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


app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to my api"}