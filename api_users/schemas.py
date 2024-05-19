# This file contains the "models" used inside of the API code itself, pretty much like springboot, except
# that these will NOT be saved to the database. They will only be used here, inside the python app.
# For instance, password is only present in the user creation class, as the created user will be saved
# to the DB, and the password won't be sent around when fetching a certain users's data (kinda like a DTO).

# Base models contain the data that will always be there and will often be needed when passing data around.
# Create models are self explanatory, they extend the base class and add something needed ONLY for creation,
# and that something will probably be stored in the DB, but not be passed around.
# Standard models are those which will be returned by the API.
# Example: User class doesn't have a password attribute, as it won't be sent when fetching.

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    display_name: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True # Used to be orm_mode = True

class CreateUserRequest(UserBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Team(BaseModel):
    id: int
    name: str
    player_ids: list[int]

    class Config:
        from_attributes = True # Used to be orm_mode = True

class CreateTeamRequest(BaseModel):
    name: str
    player_ids: list[int]