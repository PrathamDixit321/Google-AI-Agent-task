from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class DeployAgent(BaseAgent):
    """Agent responsible for deployment workflows and environment configuration.

    Responsibilities:
    - Generate deployment manifests (Docker, Kubernetes, or simple scripts)
    - Trigger deployment via tools (e.g., `github_writer`, `deployer`)
    - Report status and collect deployment logs
    """

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action", "deploy")
        params = payload.get("params", {})

        if action == "deploy":
            return await self.deploy_project(params)
        if action == "status":
            return await self.get_status(params)
        if action == "config":
            return await self.generate_deploy_config(params)
        return {"ok": False, "error": "unknown action"}

    async def deploy_project(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Trigger a deployment using available tools.

        Expects `params` to possibly include `repo`, `branch`, `target` and `strategy`.
        """
        repo = params.get("repo")
        strategy = params.get("strategy", "simple")

        deployer = self.tools.get("deployer")
        github = self.tools.get("github_writer")

        self.log("Starting deployment", repo=repo, strategy=strategy)

        # Prefer an installed deployer tool if available
        if deployer:
            try:
                result = await deployer.deploy(repo=repo, strategy=strategy, params=params)
                return {"ok": True, "deployer": True, "result": result}
            except Exception as e:
                return {"ok": False, "error": str(e)}

        # Fallback: create a simple deployment plan and optionally push to GitHub
        plan = {
            "repo": repo,
            "strategy": strategy,
            "steps": [
                "Ensure requirements are pinned",
                "Create Dockerfile",
                "Push image to registry",
                "Apply Kubernetes manifests or simplified run script",
            ],
        }

        if github and repo:
            try:
                # Example: create a deployment branch with manifests (tool contract assumed)
                await github.create_branch_and_commit(repo, branch=params.get("branch", "deploy/auto"), files=params.get("files", {}))
                plan["github_push"] = True
            except Exception:
                plan["github_push"] = False

        self.log("Prepared deployment plan", repo=repo)
        return {"ok": True, "plan": plan}

    async def get_status(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Return a deployment status. If a deployer tool is present, query it."""
        deployer = self.tools.get("deployer")
        if deployer:
            try:
                status = await deployer.status(params.get("deployment_id"))
                return {"ok": True, "status": status}
            except Exception as e:
                return {"ok": False, "error": str(e)}
        # Fallback stub
        return {"ok": True, "status": "not_deployed"}

    async def generate_deploy_config(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Produce a minimal deployment configuration (e.g., Dockerfile + manifest)."""
        language = params.get("language", "python")
        config = {
            "dockerfile": "FROM python:3.11-slim\nWORKDIR /app\nCOPY . /app\nRUN pip install -r requirements.txt\nCMD [\"python\", \"app.py\"]",
            "manifest": {"replicas": params.get("replicas", 1), "env": params.get("env", {})},
        }
        self.log("Generated deploy config", language=language)
        return {"ok": True, "config": config}
