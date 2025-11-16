# AI Personal Growth Operating System (AI-PGOS)

A FastAPI-based multi-agent AI system for personalized learning, career planning, project management, content creation, and habit tracking.

## Overview

This is a **Freestyle Track Capstone Project** for the Google AI Agent course. The system helps students and early professionals manage their growth across multiple dimensions:

- **Learning & Coding**: Personalized schedules, practice recommendations, project scaffolding
- **Career Planning**: Career path recommendations, skill gap analysis, upskilling guidance
- **Project Management**: From idea to execution, with code generation and deployment support
- **Content Creation**: Content ideas, script generation, and publishing workflows
- **Productivity & Habits**: Daily routines, habit tracking, and performance improvements
- **Long-term Memory**: Persistent session state and learning history across interactions

The system uses a **Coordinator Agent** to orchestrate requests across specialized agents and maintains observability through centralized logging.

## Project Structure

```
├─ README.md                          # This file
├─ LICENSE                            # MIT License
├─ requirements.txt                   # Python dependencies
├─ run_server.ps1                     # Start Uvicorn server (Windows)
├─ src/
│  ├─ app.py                          # FastAPI coordinator app
│  ├─ agents/
│  │  ├─ base_agent.py                # BaseAgent interface
│  │  ├─ coordinator_agent.py          # Routes tasks to specialized agents
│  │  ├─ learning_agent.py             # Learning plans & recommendations
│  │  ├─ coding_agent.py               # Project scaffolding & code execution
│  │  ├─ career_agent.py               # Career planning & skill gaps
│  │  ├─ content_agent.py              # Content ideas & scripts
│  │  ├─ productivity_agent.py          # Habits & daily routines
│  │  ├─ deploy_agent.py               # Deployment workflows
│  │  ├─ README.md                     # Agent documentation
│  │  └─ __init__.py                   # Exports all agents
│  ├─ tools/
│  │  ├─ code_runner.py                # Code execution
│  │  ├─ code_runner_stub.py           # Code runner stub (demo)
│  │  ├─ github_writer.py              # GitHub integration
│  │  ├─ deployer_stub.py              # Deployment stub (demo)
│  │  └─ search_tool.py                # Web/code search
│  ├─ memory/
│  │  ├─ memory_bank.py                # Persistent memory API
│  │  ├─ session_service.py            # Session management
│  │  └─ in_memory.py                  # In-memory demo store
│  └─ observability/
│     └─ logger.py                     # Centralized logging
├─ tests/
│  └─ test_app.py                     # Integration tests
├─ scripts/
│  └─ demo_request.py                 # Example API client
├─ templates/                         # Code templates for scaffolding
├─ demos/                             # Sample outputs
└─ docs/
   └─ writeup.md                      # System architecture & design
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone or extract the repository:
```powershell
cd "c:\Users\Admin\Desktop\Google AI Agent"
```

2. Install dependencies:
```powershell
python -m pip install -r requirements.txt
```

### Running the Server

**Option 1: Using the provided script (Windows PowerShell)**
```powershell
.\run_server.ps1
```

**Option 2: Manual start**
```powershell
$env:PYTHONPATH = "$PWD\src;$env:PYTHONPATH"
python -m uvicorn src.app:app --host 127.0.0.1 --port 8000
```

The server will be available at `http://127.0.0.1:8000`.

### Testing

Run the automated tests:
```powershell
python -m pytest tests/test_app.py -v
```

Or run the demo request (after starting the server):
```powershell
python .\scripts\demo_request.py
```

### API Endpoints

#### Health Check
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/health
```
Returns: `{"status":"ok"}`

#### Task Submission
```powershell
$payload = @{
  task_type = "learning.plan"
  user_id = "user1"
  params = @{ weekly_hours = 5 }
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/task `
  -Body $payload -ContentType "application/json"
```

### Supported Tasks

Each task is routed to the appropriate agent via `task_type` prefix:

| Agent | Task Type | Example |
|-------|-----------|---------|
| Learning | `learning.plan` | Create a learning schedule |
| Learning | `learning.recommend` | Get daily task recommendations |
| Coding | `coding.scaffold` | Generate project structure |
| Coding | `coding.run` | Execute code snippet |
| Career | `career.plan` | Create a career development plan |
| Career | `career.skills_gap` | Analyze skill gaps |
| Content | `content.ideas` | Generate content ideas |
| Content | `content.script` | Create a content script |
| Productivity | `productivity.today` | Get daily routines |
| Productivity | `productivity.track` | Log a habit completion |
| Deploy | `deploy.deploy` | Deploy a project |
| Deploy | `deploy.status` | Check deployment status |
| Deploy | `deploy.config` | Generate deploy config |

### Example: Learning Plan Task

```powershell
$learningTask = @{
  task_type = "learning.plan"
  user_id = "user123"
  params = @{
    weekly_hours = 6
  }
} | ConvertTo-Json

$response = Invoke-RestMethod -Method Post `
  -Uri http://127.0.0.1:8000/task `
  -Body $learningTask `
  -ContentType "application/json"

$response | ConvertTo-Json -Depth 10 | Write-Host
```

### Example: Content Ideas Task

```powershell
$contentTask = @{
  task_type = "content.ideas"
  params = @{
    topic = "machine learning for beginners"
  }
} | ConvertTo-Json

Invoke-RestMethod -Method Post `
  -Uri http://127.0.0.1:8000/task `
  -Body $contentTask `
  -ContentType "application/json"
```

## Architecture

### Core Components

**CoordinatorAgent**: Routes incoming tasks to the appropriate specialized agent based on the `task_type` prefix.

**Specialized Agents**:
- `LearningAgent`: Builds personalized learning plans and daily task recommendations
- `CodingAgent`: Scaffolds projects and integrates with code execution tools
- `CareerAgent`: Plans career development and identifies skill gaps
- `ContentAgent`: Generates content ideas and scripts for creators
- `ProductivityAgent`: Tracks habits and provides daily routines
- `DeployAgent`: Handles deployment configurations and status monitoring

**Memory System**: In-memory storage (demo) with extensible interfaces for persistent databases.

**Tools**: Pluggable tools for code execution, GitHub integration, and deployment.

**Logger**: Centralized structured logging using Python's standard logging.

### Request Flow

```
POST /task {task_type, user_id, params}
  ↓
CoordinatorAgent.handle()
  ↓
Route to specialized agent based on prefix
  ↓
Agent processes with access to memory, tools, logger
  ↓
Return result JSON
```

## Development

### Adding a New Agent

1. Create a new file under `src/agents/` (e.g., `my_agent.py`)
2. Subclass `BaseAgent` and implement the `handle()` method
3. Export the class in `src/agents/__init__.py`
4. Register it in `src/app.py` with the coordinator:
   ```python
   coord.register("my_prefix", MyAgent(...))
   ```

### Running Tests

```powershell
# Run all tests
python -m pytest tests/ -v

# Run a specific test
python -m pytest tests/test_app.py::test_health_ok -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html
```

### Extending Tools

Tools are registered as a dict and passed to agents. To add a new tool:

1. Create a class with async methods in `src/tools/`
2. Instantiate it and add to the `tools` dict in `src/app.py`
3. Access in agents via `self.tools.get("tool_name")`

## Demo Outputs

See `/demos` folder for sample request/response examples and use cases.

## Documentation

- `docs/writeup.md`: Detailed architecture and design decisions
- `src/agents/README.md`: Agent implementation guide
- Code comments throughout for implementation details

## Performance & Scalability

- **Current**: In-memory storage and local execution (development mode)
- **Production**: Replace `InMemoryMemory` with a real database, add authentication, scale with load balancers

## Future Enhancements

- [ ] Web UI dashboard for tracking progress
- [ ] Real-time progress tracking and WebSocket support
- [ ] Integration with Google AI APIs for richer content generation
- [ ] Persistent database backend (PostgreSQL, MongoDB)
- [ ] Authentication and multi-user isolation
- [ ] Advanced analytics and performance reports
- [ ] Mobile app support
- [ ] Integration with external APIs (Slack, Discord, email)

## Contributors

Built as a Freestyle Track Capstone Project for the Google AI Agent course.

## License

MIT License - See LICENSE file for details

---

**Questions or issues?** Check `docs/writeup.md` or review agent implementations in `src/agents/`.
