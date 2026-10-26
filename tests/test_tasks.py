from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)
@patch("src.routes.tasks.tasks_table")
def test_create_task(mock_table):
    mock_table.put_item.return_value = {}
    payload = {
        "task_id": "test-001",
        "title": "Test task",
        "description": "A task for testing",
        "completed": False,
    }
    response = client.post("/tasks/", json=payload)
    assert response.status_code in (200, 201)
    mock_table.put_item.assert_called_once()
@patch("src.routes.tasks.tasks_table")
def test_get_tasks(mock_table):
    mock_table.scan.return_value = {
        "Items": [
            {
                "task_id": "test-001",
                "title": "Test task",
                "description": "A task for testing",
                "completed": False,
            }
        ]
    }
    response = client.get("/tasks/")
    assert response.status_code == 200
    mock_table.scan.assert_called_once()
def test_home():
    response = client.get("/")
    assert response.status_code == 200