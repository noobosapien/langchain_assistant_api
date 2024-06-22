from pydantic import BaseModel
import datetime

class TaskBase(BaseModel):
    id: int
    task_name: str
    task_desc: str
    task_complete: bool
    task_due: datetime.time
    priority:str

class TaskCreate(TaskBase):
    class Config:
        orm_mode = True
