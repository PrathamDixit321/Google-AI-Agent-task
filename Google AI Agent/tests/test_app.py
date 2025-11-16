import sys
import os

# Ensure src package imports resolve during tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


def test_learning_plan_task():
    payload = {
        "task_type": "learning.plan",
        "user_id": "pytest-user",
        "params": {"weekly_hours": 4},
    }
    r = client.post("/task", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body.get("ok") is True
    assert body.get("agent") == "learning"
    result = body.get("result")
    assert result and result.get("ok") is True
    plan = result.get("plan")
    assert plan and plan.get("weekly_hours") == 4
