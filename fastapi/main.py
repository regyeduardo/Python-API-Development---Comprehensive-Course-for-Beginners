from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
# from pydantic.types import OptionalInt

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

"""
.get = method (http)
("/") = path (url)
root() = function
"""
@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}