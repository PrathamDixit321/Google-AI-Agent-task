from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent


class CoordinatorAgent(BaseAgent):
    """Orchestrates workflows across specialized agents.

    Responsibilities:
    - Register agents
    - Route tasks to the appropriate agent
    - Maintain short-term session state for an ongoing workflow
    - Aggregate responses and present a combined result
    """

    def __init__(self, name: str = "Coordinator", memory: Optional[Any] = None, tools: Optional[Dict[str, Any]] = None, logger: Optional[Any] = None) -> None:
        super().__init__(name=name, memory=memory, tools=tools, logger=logger)
        self.agents: Dict[str, BaseAgent] = {}

    def register(self, key: str, agent: BaseAgent) -> None:
        self.agents[key] = agent
        self.log(f"Registered agent '{key}'")

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Main entrypoint: expects `payload` to include a `task_type` key.

        Example payload: {"task_type": "learning.plan", "user_id": "u1", "params": {...}}
        """
        task_type = payload.get("task_type") or payload.get("type")
        if not task_type:
            return {"ok": False, "error": "missing task_type"}

        # Simple routing strategy: prefix before '.' selects agent
        prefix = task_type.split(".")[0]
        agent = self.agents.get(prefix)
        if not agent:
            return {"ok": False, "error": f"no agent registered for prefix '{prefix}'"}

        self.log(f"Routing task '{task_type}' to agent '{prefix}'", task_type=task_type)
        result = await agent.handle(payload)
        return {"ok": True, "agent": prefix, "result": result}

    def list_agents(self) -> List[str]:
        return list(self.agents.keys())
