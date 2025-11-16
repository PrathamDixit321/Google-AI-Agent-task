from typing import Any, Dict, Optional


class BaseAgent:
    """Minimal base agent interface for the AI-PGOS system.

    Provides consistent constructor params and a single async `handle` entrypoint.
    Concrete agents should subclass and implement their own behaviors.
    """

    def __init__(self, name: str, memory: Optional[Any] = None, tools: Optional[Dict[str, Any]] = None, logger: Optional[Any] = None) -> None:
        self.name = name
        self.memory = memory
        self.tools = tools or {}
        self.logger = logger

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an incoming request/task and return a response dict.

        Args:
            payload: A serializable dict describing the task or user input.

        Returns:
            A dict containing agent result and optional metadata.
        """
        raise NotImplementedError("Agents must implement `handle`")

    def log(self, message: str, **meta: Any) -> None:
        if self.logger:
            try:
                self.logger.info(f"[{self.name}] {message}", extra=meta)
            except Exception:
                # Fallback to simple print if logger fails
                print(f"[{self.name}] {message}", meta)
        else:
            print(f"[{self.name}] {message}", meta)
