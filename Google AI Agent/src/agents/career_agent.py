from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class CareerAgent(BaseAgent):
    """Agent to help with career planning and upskilling recommendations."""

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action", "plan")
        if action == "plan":
            return await self.create_career_plan(payload.get("user_id"), payload.get("params", {}))
        if action == "skills_gap":
            return await self.analyze_skill_gaps(payload.get("user_id"), payload.get("params", {}))
        return {"ok": False, "error": "unknown action"}

    async def create_career_plan(self, user_id: Optional[str], params: Dict[str, Any]) -> Dict[str, Any]:
        career_goal = params.get("goal", "software engineer")
        plan = {
            "goal": career_goal,
            "milestones": [
                {"title": "Foundational skills", "deadline_weeks": 12},
                {"title": "Build portfolio project", "deadline_weeks": 24},
                {"title": "Interview prep", "deadline_weeks": 36},
            ],
        }
        self.log("Created career plan", user_id=user_id, goal=career_goal)
        return {"ok": True, "plan": plan}

    async def analyze_skill_gaps(self, user_id: Optional[str], params: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder logic: return a minimal skills gap analysis
        return {"ok": True, "gaps": ["system design basics", "advanced algorithms"]}
