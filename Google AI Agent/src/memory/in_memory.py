from typing import Any, Dict, List, Optional
import asyncio


class InMemoryMemory:
    def __init__(self):
        self.store: Dict[str, Any] = {}
        self.habit_events: List[Dict[str, Any]] = []

    async def get(self, key: str) -> Optional[Any]:
        return self.store.get(key)

    async def set(self, key: str, value: Any) -> None:
        self.store[key] = value

    async def append_habit_event(self, habit: str, value: Any) -> None:
        self.habit_events.append({"habit": habit, "value": value})

    async def list_habit_events(self) -> List[Dict[str, Any]]:
        return list(self.habit_events)
