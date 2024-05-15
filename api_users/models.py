# This file defines the class models that will go in the database itself.
# Classes represent tables, and attributes represent columns.

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    display_name = Column(String, unique=False, index=True)
    hashed_password = Column(String)