from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session, Session
import models, schemas
from database import engine, sessionLocal, Base
from typing import List

app = FastAPI(title="User Management API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "User Management API is running", "status": "success"}

@app.get("/users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    """Get all users"""
    try:
        users = db.query(models.User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/users", response_model=dict)
def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    try:
        # Check if user with same email already exists
        existing_user = db.query(models.User).filter(models.User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        
        db_user = models.User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return {
            "message": "User saved successfully",
            "status": "success",
            "user": {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create user: {str(e)}")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}

