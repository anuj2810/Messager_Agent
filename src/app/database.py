"""
Database Connection Module

Ref: Tech Stack §1.2.4 - asyncpg pool, pool size 10-20, timeout 5 seconds
Ref: Design §2.1 - Non-blocking DB driver (asyncpg)
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass


# Async engine - Tech Stack §1.1.3: asyncpg driver
engine = create_async_engine(
    settings.database_url,
    pool_size=settings.db_pool_size,
    max_overflow=settings.db_max_overflow,
    pool_timeout=settings.db_pool_timeout,
    echo=False,
)

# Async session factory
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncSession:
    """FastAPI dependency for database session injection."""
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
