# Hello controller from springboot

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, auth, crud
from .auth import get_current_user
from .database import SessionLocal, engine

from typing import Annotated

from .schemas import User, CreateTeamRequest

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check(db: db_dependency):
    if db is None:
        raise HTTPException(status_code=503, detail='Could not connect to the database')
    return {"status": "healthy"}

@app.get("/matchmaking", status_code=status.HTTP_200_OK)
async def users_with_teams(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    query = crud.get_users_with_team(db, user.id)
    return query

@app.get("/user/me", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    return {"User": User(username=user.username, display_name=user.display_name, id=user.id)}

@app.get("/user/{id}", status_code=status.HTTP_200_OK)
async def user(id:int, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    query = crud.get_user_by_id(id)
    if query is None:
        raise HTTPException(status_code=404, detail='User was not found')
    return {"User": User(username=query.username, display_name=query.display_name, id=query.id)}

@app.post("/team", status_code=status.HTTP_201_CREATED)
async def create_team(user: user_dependency, db:db_dependency, create_team_request: CreateTeamRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    team = crud.get_user_team(db, user.id)
    if team:
        raise HTTPException(status_code=409, detail='Team already exists')
    if len(create_team_request.player_ids) != 11:
        raise HTTPException(status_code=422, detail='Team size must be 11')
    new_team = crud.create_team(db, user.id, create_team_request)
    return new_team

@app.get("/user/me/team", status_code=status.HTTP_200_OK)
async def team(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    team = crud.get_user_team(db, user.id)
    if team is None:
        raise HTTPException(status_code=404, detail='No team found')
    return team

@app.get("/user/{id}/team", status_code=status.HTTP_200_OK)
async def get_team(id: int, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    query = crud.get_user_by_id(db, id)
    if query is None:
        raise HTTPException(status_code=404, detail='User was not found')
    team = crud.get_user_team(db, id)
    if team is None:
        raise HTTPException(status_code=404, detail='No team found')
    return team