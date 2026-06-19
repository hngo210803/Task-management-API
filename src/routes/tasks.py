from fastapi import APIRouter, HTTPException
from datetime import datetime, UTC
from uuid import uuid4

from src.models.task import Task, TaskCreate, TaskUpdate
from src.services.dynamodb import tasks_table

router = APIRouter()

 # TODO: migrate remaining CRUD operations to DynamoDB
tasks_db = {} # temporary local storage for GET/PUT/DELETE during migration

@router.post("/tasks", response_model=Task) #TẠO Khi có request POST /tasks
def create_task(task: TaskCreate): #When client sends a request POST to /tasks, FastAPI will call create_task()

    new_task = Task (
        task_id= str(uuid4()), #uuid4() creates one unique id for each task
        title = task.title,
        description=task.description,
        status = task.status,
        created_at = datetime.now(UTC)
    )
    tasks_table.put_item(
        Item=new_task.model_dump(mode="json")
    )
    return new_task

@router.get("/tasks") #LẤY ALL
def get_tasks():
    response = tasks_table.scan()
    return response["Items"]

@router.get("/tasks/{task_id}")

def get_task(task_id: str): #LẤY 1 TASK
    response=tasks_table.get_item(Key= {"task_id": task_id})
    if "Item" not in response:
        raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
    return response["Item"] #Trả về duy nhất 1 task nên phải là Item số ít

@router.put("/tasks/{task_id}") #CẬP NHẬT
def update_task(task_id: str, task_update: TaskUpdate):
    response=tasks_table.get_item(Key= {"task_id": task_id}) #Lấy tast từ DynamoDB, và chỉ trả về 1 task duy nhất nên đó là Item, khác với scan, trả về 1 bảng tasks -> Items
   #Kiểm tra task có tồn tại không
    if "Item" not in response:
        raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
   #Tạo updated data
 
    item = response["Item"]

    if task_update.title is not None:
        item["title"] = task_update.title

    if task_update.description is not None:
        item["description"] = task_update.description

    if task_update.status is not None:
        item["status"] = task_update.status
    tasks_table.put_item(   #ghi lại bằng put_item
       Item = item ) #Áp dụng các field mới từ task_update
    return item


@router.delete("/tasks/{task_id}") #XOÁ

def delete_task(task_id: str):
    response=tasks_table.get_item(Key= {"task_id": task_id})
    if "Item" not in response:
        raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
    tasks_table.delete_item( 
        Key={"task_id": task_id})
    return {"message": "Task has been deleted successfully"}
             