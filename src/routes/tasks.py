from fastapi import APIRouter, HTTPException
from datetime import datetime, UTC
from uuid import uuid4

from src.models.task import Task, TaskCreate, TaskUpdate

router = APIRouter()

tasks_db = {} # create database for ram

@router.post("/tasks", response_model=Task) #TẠO Khi có request POST /tasks
def create_task(task: TaskCreate): #When client sends a request POST to /tasks, FastAPI will call create_task()

    new_task = Task (
        task_id= str(uuid4()), #uuid4() creates one unique id for each task
        title = task.title,
        description=task.description,
        status = task.status,
        created_at = datetime.now(UTC)
    )
    tasks_db[new_task.task_id] = new_task #save new_task to database
    return new_task

@router.get("/tasks") #LẤY ALL
def get_tasks():
    return list(tasks_db.values())

@router.get("/tasks/{task_id}")

def get_task(task_id: str): #LẤY 1 TASK
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@router.put("/tasks/{task_id}") #CẬP NHẬT
def update_task(task_id: str, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db[task_id]
    updated_data = task.model_dump() #Conserve the champs not sent in the request and only modify what is given 
    if task_update.title is not None:
         updated_data["title"] = task_update.title
    if task_update.description is not None:
        updated_data["description"] = task_update.description
    if task_update.status is not None:
        updated_data["status"] = task_update.status
    updated_task = Task(**updated_data) #Create object Task again
    tasks_db[task_id] = updated_task
    return updated_task


@router.delete("/tasks/{task_id}") #XOÁ

def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task has been deleted successfully"}
             