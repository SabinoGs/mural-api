from typing import List
from fastapi import FastAPI, Depends, HTTPException
from mural_api.sql.config import SessionLocal, engine
from sqlalchemy.orm import Session
from mural_api.apps.models import Base
from mural_api.apps.schemas import User, UserCreate 
from mural_api.apps.crud import create_user 

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)

    if db_user:
        raise HTTPException(status=400, detail="User Already registered")
    
    return create_user(db=db, user=user)
