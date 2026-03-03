# 🤖 AI Messenger Agent

**AI-powered personal style-based auto-reply system for WhatsApp**

An intelligent messaging automation system that responds to incoming WhatsApp messages in your authentic communication style — adjusting tone per relationship, learning from your corrections, and preserving your natural conversational personality.

---

## 📌 Project Status

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1 – Document Analysis & Roadmap | ✅ Complete | 4/4 tasks |
| Phase 2 – Environment & Foundation Setup | ✅ Complete | 5/5 tasks |
| Phase 3 – Database Implementation | 🔨 In Progress | 2/5 tasks |
| Phase 4 – Backend Core Setup | ⬜ Not Started | 0/5 tasks |
| Phase 5 – WhatsApp Integration | ⬜ Not Started | 0/4 tasks |
| Phase 6 – AI Prompt Engine | ⬜ Not Started | 0/5 tasks |
| Phase 7 – Personality Modeling Engine | ⬜ Not Started | 0/4 tasks |
| Phase 8 – Agent State Management | ⬜ Not Started | 0/4 tasks |
| Phase 9 – Security Hardening | ⬜ Not Started | 0/4 tasks |
| Phase 10 – Observability & Logging | ⬜ Not Started | 0/3 tasks |
| Phase 11 – Deployment Setup | ⬜ Not Started | 0/4 tasks |
| Phase 12 – Testing & Validation | ⬜ Not Started | 0/4 tasks |
| Phase 13 – Production Readiness | ⬜ Not Started | 0/2 tasks |

**Overall: 11 / 49 tasks completed**

---

## 🏗 Architecture

The system follows a **5-layer modular monolith** architecture:

```
┌─────────────────────────────────┐
│        Router Layer             │  ← FastAPI endpoints
├─────────────────────────────────┤
│        Service Layer            │  ← Business logic orchestration
├─────────────────────────────────┤
│        Domain Layer             │  ← AI personality, tone engine, prompt builder
├─────────────────────────────────┤
│        Repository Layer         │  ← Database abstraction (async)
├─────────────────────────────────┤
│        Integration Layer        │  ← WhatsApp API, OpenAI API
└─────────────────────────────────┘
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI (async) |
| **Database** | PostgreSQL 15+ (with pgvector) |
| **ORM** | SQLAlchemy 2.0 (async) + Alembic |
| **AI Provider** | OpenAI API (GPT-4o-mini) |
| **Messaging** | WhatsApp Business API |
| **HTTP Client** | httpx (async) |
| **Deployment** | Docker + Nginx + AWS EC2 |
| **CI/CD** | GitHub Actions |
| **Dependency Mgmt** | Poetry |

---

## 📁 Project Structure

```
Messager_Agent/
├── docs/                          # Documentation
│   ├── PRD.md                     # Product Requirements Document
│   ├── ARCHITECTURE.md            # System Architecture Document
│   ├── DESIGN.md                  # System Design Document
│   ├── TECH_STACK.md              # Tech Stack & Infrastructure
│   ├── Database_Design.md         # Database Schema Deep Design
│   ├── AI_Personality_Modeling_Philosophy.md  # AI Prompt Engineering
│   ├── Security_Architecture.md   # Security & Compliance
│   └── Execution_Plan/            # Task-by-task execution docs (Hinglish)
│       ├── task1.md               # Poetry & dependency setup
│       └── task2.md               # Layered architecture skeleton
├── src/
│   └── app/
│       ├── main.py                # FastAPI entry point
│       ├── config.py              # Pydantic settings (env vars)
│       ├── database.py            # Async SQLAlchemy engine + pool
│       ├── routers/               # API endpoints (webhook, agent)
│       ├── services/              # Business logic (pending)
│       ├── domain/                # Core AI/personality logic (pending)
│       ├── repositories/          # DB operations (pending)
│       ├── integrations/          # External APIs (pending)
│       ├── models/                # SQLAlchemy ORM models (pending)
│       └── schemas/               # Pydantic request/response models
│           └── common.py          # Standard error model
├── tests/
│   ├── unit/                      # Unit tests (pending)
│   ├── integration/               # Integration tests (pending)
│   ├── ai/                        # AI prompt tests (pending)
│   └── load/                      # Load tests (pending)
├── .env.example                   # Environment variables template
├── Dockerfile                     # Multi-stage Docker build
├── docker-compose.yml             # 3 services: app + db + nginx
├── initdb/                        # Database initialization scripts
│   └── 01-init.sql                # Setup pgvector and app_user
├── alembic_migrations/            # Alembic async migration environment
├── alembic.ini                    # Alembic config point to alembic_migrations
├── pyproject.toml                 # Poetry project config
├── poetry.lock                    # Locked dependency versions
├── TODO.md                        # Full task checklist (49 tasks)
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

### Key Config Variables (from `.env.example`)
```
DATABASE_URL          → PostgreSQL connection string
OPENAI_API_KEY        → OpenAI API authentication
WHATSAPP_API_TOKEN    → WhatsApp Business API token
WHATSAPP_APP_SECRET   → Webhook HMAC verification secret
TOKEN_BUDGET_TOTAL    → Max 1200 input tokens for LLM
CONTEXT_WINDOW_SIZE   → Last 5 messages sliding window
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Poetry

### Installation
```bash
# Clone the repository
git clone https://github.com/anuj2810/Messager_Agent.git
cd Messager_Agent

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

### Running (coming soon)
```bash
# Start development server
poetry run uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📚 Documentation

- **[TODO.md](./TODO.md)** — Full 49-task execution checklist
- **[docs/Execution_Plan/](./docs/Execution_Plan/)** — Beginner-friendly task explanations (Hindi + English)
- **[docs/PRD.md](./docs/PRD.md)** — Product Requirements Document
- **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)** — System Architecture
- **[docs/DESIGN.md](./docs/DESIGN.md)** — System Design Document

---

## 🔑 Key Features (MVP Scope)

- ✅ WhatsApp Business API integration
- ✅ Global & per-contact AI toggle
- ✅ Real-time AI auto-reply (<3 seconds)
- ✅ Relationship-aware tone modeling (8 personality traits)
- ✅ Review mode (approve before sending)
- ✅ Learning from user corrections
- ✅ Human-like response delay simulation
- ✅ Structured audit logging
- ✅ Dockerized deployment

---

## 📄 License

This project is proprietary and confidential.

---

*Last updated: 2026-03-03 — Tasks 1-7 completed (Database models, pgvector tracking, configs, UUID rules & Alembic scaffolding done)*
