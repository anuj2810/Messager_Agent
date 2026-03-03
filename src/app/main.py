"""
AI Messenger Agent - Main Application Entry Point

FastAPI application with modular monolith architecture.
Ref: Architecture §1.3, Tech Stack §1.1.2, Design §2.1
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import webhook, agent


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown events."""
    # Startup: Initialize DB pool, load config
    yield
    # Shutdown: Close DB pool, cleanup


app = FastAPI(
    title="AI Messenger Agent",
    description="AI-powered personal style-based auto-reply system",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS Middleware - Security §9: CORS restricted
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],  # Restrict in production
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Register Routers - Tech Stack §1.1.5: Router Layer
app.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])
app.include_router(agent.router, prefix="/agent", tags=["Agent Control"])


@app.get("/health", tags=["System"])
async def health_check():
    """System health check endpoint."""
    return {"status": "healthy", "service": "ai-messenger-agent"}
