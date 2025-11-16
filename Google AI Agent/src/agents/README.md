# Agents

This folder contains the core agent modules for the AI Personal Growth Operating System (AI-PGOS).

Files:
- `base_agent.py`: BaseAgent interface and common utilities.
- `coordinator_agent.py`: Orchestrates tasks and routes to specialized agents.
- `learning_agent.py`: Creates personalized learning plans and daily recommendations.
- `coding_agent.py`: Manages scaffolding, project workflows and code execution hooks.
- `career_agent.py`: Career planning and skills-gap analysis.
- `content_agent.py`: Content idea generation and scripts.
- `productivity_agent.py`: Habit tracking and productivity suggestions.

Next steps:
- Wire these agents into `src/app.py` using a `CoordinatorAgent` instance.
- Provide concrete implementations for memory, tools (code runner, search), and observability logger.
- Add tests and example flows demonstrating an end-to-end user request.
