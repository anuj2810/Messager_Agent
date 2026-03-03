# ============================================================
# AI Messenger Agent - Multi-Stage Dockerfile
# ============================================================
# Ref: Design §13 - Multi-stage Docker build
# Ref: Architecture §9 - Containerized FastAPI app
# ============================================================

# --- Stage 1: Builder ---
FROM python:3.10-slim AS builder

WORKDIR /build

# Install Poetry
RUN pip install --no-cache-dir poetry==2.3.2

# Copy dependency files first (Docker layer caching)
COPY pyproject.toml poetry.lock ./

# Export dependencies to requirements.txt (no dev deps)
RUN poetry export -f requirements.txt --without dev --output requirements.txt

# --- Stage 2: Runtime ---
FROM python:3.10-slim AS runtime

# Security: Run as non-root user
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

# Install only production dependencies
COPY --from=builder /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/health')" || exit 1

# Run FastAPI via Uvicorn
# Ref: Tech Stack §1.1.3 - Uvicorn workers, asyncio event loop
CMD ["python", "-m", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
