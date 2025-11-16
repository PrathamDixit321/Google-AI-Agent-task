from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class ContentAgent(BaseAgent):
    """Agent that generates content ideas, outlines, and scripts for creators."""

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action", "ideas")
        if action == "ideas":
            return await self.generate_ideas(payload.get("params", {}))
        if action == "script":
            return await self.generate_script(payload.get("params", {}))
        return {"ok": False, "error": "unknown action"}

    async def generate_ideas(self, params: Dict[str, Any]) -> Dict[str, Any]:
        topic = params.get("topic", "learning to code")
        ideas = [f"Top 10 tips for {topic}", f"A week-long challenge: {topic}", f"Interview with an expert on {topic}"]
        return {"ok": True, "topic": topic, "ideas": ideas}

    async def generate_script(self, params: Dict[str, Any]) -> Dict[str, Any]:
        title = params.get("title", "Quick Tips")
        script = f"Intro: Today we'll talk about {title}.\nPoint 1: ...\nConclusion: ..."
        return {"ok": True, "title": title, "script": script}
