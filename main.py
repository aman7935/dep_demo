from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session, Session
import models, schemas
from database import engine, sessionLocal, Base

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()



@app.post("/users")
def createUser(user: schemas.userCreate, db: Session = Depends(get_db)):

    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "user saved successfully"}

