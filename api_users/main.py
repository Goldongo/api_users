# Hello controller from springboot

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, auth, crud
from .auth import get_current_user
from .database import SessionLocal, engine

from typing import Annotated

from .schemas import User

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    userData = crud.get_user_by_id(db, user['id'])
    return {"User": User(username=userData.username, display_name=userData.display_name, id=userData.id)}
