from pydantic import BaseModel  # pylint: disable=no-name-in-module
from datetime import datetime

class PostBase(BaseModel):  # pylint: disable=missing-class-docstring
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True