from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Created by pytest",
            "status": "pending"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Created by pytest"
    assert data["status"] == "pending"
    assert "task_id" in data


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)