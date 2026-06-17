from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Task (BaseModel): #Một task phải có những thuộc tính gì
    task_id: str
    title: str
    description: str
    status: str
    created_at: datetime

class TaskCreate (BaseModel): #Khi tạo task phải gửi gì
    title: str
    description: str
    status: str = "pending"

class TaskUpdate (BaseModel): #Khi cập nhật task, client được phép gửi gì
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None