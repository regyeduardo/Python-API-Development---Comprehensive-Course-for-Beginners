from typing import List
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix='/posts', tags=['Posts'])


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.Post)
def create_posts(
        post: schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email)
    new_post = models.Post(**post.dict())  # Not added to the db yet
    db.add(new_post)
    db.commit()  # Saving post in db
    db.refresh(new_post)  # It's the same of 'RETURNING *'
    return new_post


@router.get("/", response_model=List[schemas.Post])
def get_posts(
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", response_model=schemas.Post)
def get_post(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(
        models.Post).filter(models.Post.id == id).first()  # filter = where

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )

    post.delete(synchronize_session=False)
    db.commit()
    return {"status": Response(status_code=status.HTTP_204_NO_CONTENT)}


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int,
                updated_post: schemas.PostUpdate,
                db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
