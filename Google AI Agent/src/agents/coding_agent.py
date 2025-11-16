from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class CodingAgent(BaseAgent):
    """Agent that manages project creation, scaffolding, and code execution.

    Intended to integrate with `tools.code_runner` and `templates` for scaffolding.
    """

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action", "scaffold")
        if action == "scaffold":
            return await self.scaffold_project(payload.get("params", {}))
        if action == "run":
            return await self.run_code(payload.get("params", {}))
        return {"ok": False, "error": "unknown action"}

    async def scaffold_project(self, params: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder: create a minimal project scaffold description
        project = {"name": params.get("name", "untitled"), "language": params.get("language", "python")}
        self.log("Scaffolded project", project=project)
        return {"ok": True, "project": project}

    async def run_code(self, params: Dict[str, Any]) -> Dict[str, Any]:
        # Example integration point with a code runner tool if provided
        runner = self.tools.get("code_runner")
        code = params.get("code")
        if not code:
            return {"ok": False, "error": "no code provided"}
        if runner:
            try:
                result = await runner.run(code)
                return {"ok": True, "output": result}
            except Exception as e:
                return {"ok": False, "error": str(e)}
        # Fallback: echo the code
        return {"ok": True, "output": f"(no runner) code length={len(code)}"}
