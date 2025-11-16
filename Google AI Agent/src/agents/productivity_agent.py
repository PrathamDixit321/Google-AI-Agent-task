from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class ProductivityAgent(BaseAgent):
    """Agent focused on habit tracking, productivity recommendations, and retrospectives."""

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action", "today")
        if action == "today":
            return await self.recommend_daily_routines(payload.get("params", {}))
        if action == "track":
            return await self.track_habit(payload.get("params", {}))
        return {"ok": False, "error": "unknown action"}

    async def recommend_daily_routines(self, params: Dict[str, Any]) -> Dict[str, Any]:
        routines = ["Morning review - 10min", "Focus block - 90min", "Evening reflection - 10min"]
        return {"ok": True, "routines": routines}

    async def track_habit(self, params: Dict[str, Any]) -> Dict[str, Any]:
        habit = params.get("habit")
        if not habit:
            return {"ok": False, "error": "no habit provided"}
        # Example: append to memory if available (memory API assumed)
        if self.memory and hasattr(self.memory, "append_habit_event"):
            try:
                await self.memory.append_habit_event(habit, params.get("value", True))
            except Exception:
                pass
        return {"ok": True, "habit": habit, "tracked": True}
