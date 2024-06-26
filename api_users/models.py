# This file defines the class models that will go in the database itself.
# Classes represent tables, and attributes represent columns.

import json
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.types import TypeDecorator

from .database import Base

# Create a custom JSON TypeDecorator for SQLite
class JSONEncodedList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '[]'
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        return json.loads(value)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    display_name = Column(String, unique=False, index=True)
    hashed_password = Column(String)
    team = relationship("Team", back_populates="user", uselist=False)


class Team(Base):
    __tablename__ = "teams"

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String)
    player_ids = Column(MutableList.as_mutable(JSONEncodedList))  # Store player IDs as a JSON array

    # Establishing a one-to-one relationship with the User table
    user = relationship("User", back_populates="team")