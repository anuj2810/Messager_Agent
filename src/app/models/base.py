import uuid
from datetime import datetime, timezone
from sqlalchemy import DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass


class UUIDPrimaryKeyMixin:
    """Mixin for UUID primary key (UUIDv4) with gen_random_uuid()."""
    # Ref: Database Design §1.9 UUIDs -> PostgreSQL 15 uuid/gen_random_uuid()
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )


class TimestampMixin:
    """Mixin for created_at and updated_at audit columns."""
    # Ref: Database Design §1.10 Temporal Data
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("now()")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("now()"),
        onupdate=lambda: datetime.now(timezone.utc)
    )

class SoftDeleteMixin:
    """Mixin for soft deletes."""
    # Ref: Database Design §3.5 Soft Deletion Pattern
    is_deleted: Mapped[bool] = mapped_column(default=False, server_default="false")
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
