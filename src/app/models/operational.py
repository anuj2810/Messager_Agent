from sqlalchemy import String, ForeignKey, Float, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class FeedbackCorrection(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    User feedback for an AI response, driving future style updates.
    Ref: Database Design §2.11
    """
    __tablename__ = "feedback_corrections"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    message_id: Mapped[str] = mapped_column(ForeignKey("messages.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    original_text: Mapped[str] = mapped_column(Text, nullable=False)
    corrected_text: Mapped[str] = mapped_column(Text, nullable=False)
    
    diff_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    correction_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    confidence_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Relationships
    message: Mapped["Message"] = relationship("Message", back_populates="feedback", uselist=False)


class AuditLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    System audit logs for tracking entity state changes.
    Ref: Database Design §2.12
    """
    __tablename__ = "audit_logs"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    
    entity_type: Mapped[str] = mapped_column(String(100), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(36), nullable=False) # Supporting both UUID and external IDs
    action: Mapped[str] = mapped_column(String(50), nullable=False)
    
    metadata_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class SystemConfig(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Dynamic configuration key-value storage.
    Ref: PRD Requirements (Implied operational configs).
    """
    __tablename__ = "system_configs"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    config_key: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    config_value: Mapped[dict] = mapped_column(JSON, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
