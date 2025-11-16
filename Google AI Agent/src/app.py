from fastapi import FastAPI
import asyncio

from agents import (
	CoordinatorAgent,
	LearningAgent,
	CodingAgent,
	CareerAgent,
	ContentAgent,
	ProductivityAgent,
	DeployAgent,
)
from observability.logger import get_logger
from tools.deployer_stub import DeployerStub
from tools.code_runner_stub import CodeRunnerStub
from memory.in_memory import InMemoryMemory


def create_app() -> FastAPI:
	logger = get_logger()
	app = FastAPI(title="AI-PGOS - Google AI Agent Demo")

	# Setup core infra
	memory = InMemoryMemory()
	tools = {"deployer": DeployerStub(), "code_runner": CodeRunnerStub()}

	# Create coordinator and register agents
	coord = CoordinatorAgent(memory=memory, tools=tools, logger=logger)
	coord.register("learning", LearningAgent(name="Learning", memory=memory, tools=tools, logger=logger))
	coord.register("coding", CodingAgent(name="Coding", memory=memory, tools=tools, logger=logger))
	coord.register("career", CareerAgent(name="Career", memory=memory, tools=tools, logger=logger))
	coord.register("content", ContentAgent(name="Content", memory=memory, tools=tools, logger=logger))
	coord.register("productivity", ProductivityAgent(name="Productivity", memory=memory, tools=tools, logger=logger))
	coord.register("deploy", DeployAgent(name="Deploy", memory=memory, tools=tools, logger=logger))

	@app.get("/health")
	async def health():
		return {"status": "ok"}

	@app.post("/task")
	async def run_task(payload: dict):
		# Route task through coordinator
		return await coord.handle(payload)

	# Attach coordinator to app for interactive use
	app.state.coordinator = coord
	app.state.memory = memory
	app.state.tools = tools
	app.state.logger = logger

	return app


app = create_app()

if __name__ == "__main__":
	import uvicorn

	uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=False)

