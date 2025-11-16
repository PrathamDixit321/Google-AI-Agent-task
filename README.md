AI-PGOS
AI Personal Growth Operating System (Freestyle Track – Capstone Project)

A Multi-Agent AI System for Learning, Career, Productivity & Personal Growth

1. Overview

AI-PGOS is a multi-agent AI operating system designed for students and early professionals who struggle to manage learning schedules, coding practice, career planning, content creation, project development, and productivity habits — all at the same time.

This system acts as a Personal Growth Operating System, automating planning, execution, task management, habit tracking, and continuous improvement.

AI-PGOS is built as a Freestyle Track Capstone Project for the Google AI Agent Developer Course, demonstrating:

Multi-agent systems

Parallel & sequential orchestration

Memory (long-term & session-based)

Custom tools

Observability

Evaluation loops

Code execution & search integration

Context management

Agent deployment

2. Problem Statement

Students and early-career professionals struggle to manage multiple responsibilities at once:

Learning consistency

Coding practice

Building real projects

Career planning & resumes

Creating content

Managing productivity & habits

Tracking progress over time

Most tools solve one of these problems.
None provide an integrated system that plans your life, executes tasks, tracks progress, and adapts based on performance.

This leads to:

overwhelm

lack of consistency

no long-term progress visualization

difficulty forming habits

poor productivity

unclear career direction

3. Solution — AI Personal Growth Operating System (AI-PGOS)

AI-PGOS is a multi-agent AI system that acts as your personal assistant for growth.

It:

Creates personalized learning schedules

Designs structured coding practice

Helps plan your career & upskilling roadmap

Handles end-to-end project building

Generates content ideas/scripts

Tracks habits & productivity daily

Provides actionable daily plans

Stores long-term memory about your progress

Adjusts recommendations using evaluation loops

4. System Architecture
High Level Multi-Agent Architecture
                          ┌───────────────────────────┐
                          │      Coordinator Agent     │
                          └──────────┬────────────────┘
                                     │
 ┌────────────────────┬──────────────┼───────────────┬──────────────────────┐
 │                    │              │               │                      │
 ▼                    ▼              ▼               ▼                      ▼
Learning Agent   Coding/Project   Career Agent   Content Agent   Productivity & Habits Agent
                     Agent
 │                    │              │               │                      │
 └──────────┬─────────┴──────┬──────┴─────┬────────┴────────────┬─────────┘
            │                │            │                      │
            ▼                ▼            ▼                      ▼
   Long-Term Memory     Sessions & State       Evaluation & Improvement Loop

5. Agent Responsibilities
1. Coordinator Agent

Orchestrates all other agents

Handles parallel & sequential workflows

Performs context compaction and routing

Ensures memory persistence

2. Learning Agent

Creates personalized learning schedules

Tracks progress

Adjusts topics dynamically

Uses search tools to fetch resources

Stores learning history in memory

3. Coding / Project Agent

Generates coding practice routines

Recommends problems

Helps build projects from idea → execution

Uses code execution tools

Provides debugging support

4. Career Agent

Builds resume bullet points

Tracks career progress

Suggests upskilling pathways

Prepares interview plans

Uses search tools for job info

5. Content Agent

Generates monthly content calendars

Creates scripts for reels/posts/blogs

Suggests trending topics

Maintains consistency with brand identity

6. Productivity & Habits Agent

Tracks daily habits

Generates weekly productivity reports

Identifies weak areas

Provides daily actionable recommendations

6. Core Course Concepts Implemented
✔ Multi-Agent System

6 specialized agents + coordinator agent

Parallel search & sequential task execution

✔ Custom Tools

Code Execution Tool

Search Tool

Calendar/Schedule Generator Tool

Task Manager Tool

✔ Memory

Long-Term Memory (FAISS/JSON/SQLite)

Session Memory (active dialogue state)

✔ Observability

Logging agent actions

Metrics: latency, success rate, improvement rate

Trace IDs for each agent call

✔ Evaluation Loop

Weekly performance review

Recomputes productivity score

Adjusts schedules and recommendations

✔ Deployment

API via FastAPI or Flask

Optional UI (React/Next.js or minimal HTML)

7. Tech Stack

Python 3.10+

FastAPI – API framework

LLM (OpenAI/Google Gemini) – agent intelligence

FAISS / SQLite – long-term memory storage

Redis – session memory

pydantic – schemas

docker – optional sandbox

8. Project Folder Structure
ai-pgos/
│
├── src/
│   ├── coordinator/
│   │   └── coordinator_agent.py
│   │
│   ├── agents/
│   │   ├── learning_agent.py
│   │   ├── coding_project_agent.py
│   │   ├── career_agent.py
│   │   ├── content_agent.py
│   │   └── productivity_agent.py
│   │
│   ├── tools/
│   │   ├── search_tool.py
│   │   ├── code_execution_tool.py
│   │   ├── scheduler_tool.py
│   │   └── memory_tool.py
│   │
│   ├── memory/
│   │   ├── long_term_memory.db / faiss_index
│   │   └── session_memory.py
│   │
│   ├── evaluation/
│   │   └── improvement_engine.py
│   │
│   ├── observability/
│   │   ├── logger.py
│   │   └── metrics.py
│   │
│   └── api/
│       └── app.py
│
├── docs/
│   └── architecture.png (generated diagram)
│
├── README.md
└── requirements.txt

9. Implementation Outline
Step 1 — Build Coordinator Agent

Handles:

routing

multi-agent orchestration

memory retrieval

context compaction

Step 2 — Implement Tools

Search Tool

Code Execution Tool

Scheduler Tool

Memory Tool

Step 3 — Implement Individual Agents

Each agent:

has its own system prompt

uses tools

stores output in long-term memory

is stateless (state is externalized)

Step 4 — Add Long-Term Memory

Store:

learning progress

solved coding problems

project milestones

career goals

habits/streaks

Step 5 — Create Evaluation Loop

Runs weekly:

reads memory

identifies progress gaps

adjusts next week’s schedule

Step 6 — Observability

Log:

agent actions

tool call history

latency

improvement delta

Step 7 — Optional UI

Weekly dashboard

Daily tasks

Habit tracking

Learning timeline

10. Example End-to-End Flow

User: “Optimize my next 7 days for learning AI, coding, career, and productivity.”

System Flow:

Coordinator receives the request.

Coordinator passes learning tasks → Learning Agent.

Coding plan → Coding Agent.

Career goals → Career Agent.

Content ideas → Content Agent.

Habits → Productivity Agent.

All outputs stored in long-term memory.

Coordinator merges results into a single weekly plan.

Evaluation loop checks last week’s performance and adjusts.

11. Submission Requirements (Met)

✔ Multi-Agent System

✔ Tools (search, code exec)

✔ Memory (session + long-term)

✔ Context engineering

✔ Observability

✔ Deployment-ready API

✔ Evaluation loop

✔ Freestyle Track creativity

12. Future Improvements

Add voice-based daily assistant

Integrate calendar APIs (Google Calendar, Notion)

Add full mobile UI

More agents (finance, health, relationships)

13. Conclusion

AI-PGOS is a powerful, modular, scalable multi-agent system designed to automate personal growth for students and early professionals.
It is built to be simple to extend, easy to modify, and aligned with the Google AI Agent Capstone requirements.
