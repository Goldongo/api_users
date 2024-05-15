# Here is the actual API code, sorta like your usual springboot service.

from sqlalchemy.orm import Session

from . import models

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.username == email).first()

def get_user_by_display_name(db: Session, display_name: str, limit: int = 100):
    return db.query(models.User).filter(models.User.display_name == display_name).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()