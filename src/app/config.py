"""
Application Configuration

Ref: Tech Stack §1.1.4 - pydantic-settings for environment management
Ref: Security §4 - No hardcoded secrets, secure secrets handling

All settings loaded from environment variables / .env file.
See .env.example for all available configuration options.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Priority order:
    1. Environment variables (highest)
    2. .env file
    3. Default values (lowest)
    """

    # --- Application ---
    app_name: str = "AI Messenger Agent"
    debug: bool = False
    secret_key: str = "change-me-in-production"

    # --- Database (PostgreSQL 15+) ---
    # Ref: Tech Stack §1.2.4 - asyncpg pool, pool size 10-20, timeout 5s
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/messenger_agent"
    db_pool_size: int = 10
    db_max_overflow: int = 10
    db_pool_timeout: int = 5

    # --- WhatsApp Business API ---
    # Ref: Architecture §2.2, Security §3.1
    whatsapp_api_token: str = ""
    whatsapp_phone_number_id: str = ""
    whatsapp_verify_token: str = ""
    whatsapp_app_secret: str = ""
    whatsapp_api_url: str = "https://graph.facebook.com/v18.0"

    # --- OpenAI API ---
    # Ref: Tech Stack §1.3.1, §1.3.2
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.7
    openai_max_tokens: int = 300
    openai_timeout: float = 2.5

    # --- LLM Circuit Breaker ---
    # Ref: Architecture §3.7, Design §2.6
    llm_max_retries: int = 2
    llm_circuit_breaker_threshold: int = 3
    llm_circuit_breaker_timeout: int = 30

    # --- AI Context & Token Budget ---
    # Ref: AI Modeling §4.2
    token_budget_total: int = 1200
    token_budget_output: int = 300
    token_budget_personality: int = 200
    token_budget_context: int = 700
    context_window_size: int = 5

    # --- Delay Simulation ---
    # Ref: Architecture §3.9
    delay_min_ms: int = 500
    delay_max_ms: int = 2000

    # --- Rate Limiting ---
    # Ref: Security §9
    rate_limit_per_minute: int = 60

    # --- Logging ---
    # Ref: Tech Stack §4.1
    log_level: str = "INFO"
    log_retention_days: int = 30

    # --- Observability SLOs ---
    # Ref: Architecture §11, Design §11
    slo_response_time_ms: int = 3000
    slo_error_rate_percent: float = 1.0

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


# Singleton instance - import this across the application
settings = Settings()
