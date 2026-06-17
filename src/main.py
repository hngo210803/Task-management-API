from fastapi import FastAPI
from src.routes.tasks import router

app = FastAPI(
    title = "Task Management API"
)

app.include_router(router)

@app.get("/")
def check():
    return {"message": "API is running successfully"}