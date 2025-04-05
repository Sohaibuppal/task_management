from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
from models import Task, User

api_router = APIRouter()

@api_router.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    return current_user.tasks

@api_router.post("/tasks")
def create_task(title: str, description: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = Task(title=title, description=description, owner=current_user)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task