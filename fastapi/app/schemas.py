from pydantic import BaseModel  # pylint: disable=no-name-in-module

class PostBase(BaseModel):  # pylint: disable=missing-class-docstring
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass