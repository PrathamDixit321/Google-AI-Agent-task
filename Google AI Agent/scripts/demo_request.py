import requests
import json

BASE = "http://127.0.0.1:8000"

print(requests.get(f"{BASE}/health").json())

payload = {
    "task_type": "learning.plan",
    "user_id": "demo-user",
    "params": {"weekly_hours": 3}
}
print(requests.post(f"{BASE}/task", json=payload).json())
