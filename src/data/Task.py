from sqlalchemy import Boolean, Column , Date, Integer, String
from sqlalchemy.orm import Session
from data.db import Base
import schemas

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task_name = Column(String, index=True)
    task_desc = Column(String)
    task_complete=Column(Boolean, default=False)
    task_due=Column(Date)
    priority=Column(String)

def create_task(db: Session, task: schemas.TaskCreate):
    db_item = Task(**task.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

def get_tasks(db: Session, skip: int = 0, limit:int = 100):
    return db.query(Task).offset(skip).limi(limit).all()
