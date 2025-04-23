from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    title: str

class TaskCreate(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    status: str = "not_started"
    project_id: int

class TaskUpdate(BaseModel):
    id: int
    title: str
    start_date: datetime
    end_date: datetime
    status: str
