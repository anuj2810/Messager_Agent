"""
Application Configuration

Ref: Tech Stack §1.1.4 - pydantic-settings
Ref: Security §4 - No hardcoded secrets

Full implementation in Task 3. This is a minimal stub
required for the application skeleton to be importable.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "AI Messenger Agent"
    debug: bool = False

    # Database - Tech Stack §1.2.4
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/messenger_agent"
    db_pool_size: int = 10
    db_max_overflow: int = 10
    db_pool_timeout: int = 5

    # WhatsApp API
    whatsapp_api_token: str = ""
    whatsapp_phone_number_id: str = ""
    whatsapp_verify_token: str = ""
    whatsapp_app_secret: str = ""

    # OpenAI - Tech Stack §1.3
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.7
    openai_max_tokens: int = 300
    openai_timeout: float = 2.5

    # Security
    secret_key: str = "change-me-in-production"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


settings = Settings()
