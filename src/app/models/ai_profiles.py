from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

from .base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class UserGlobalStyleProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Global AI personality definition for a user.
    Ref: Database Design §2.4
    """
    __tablename__ = "user_global_style_profile"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    style_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    # Using pgvector Vector type for embedding representation
    tone_vector: Mapped[list[float] | None] = mapped_column(Vector(1536), nullable=True)
    correction_weight: Mapped[float] = mapped_column(default=1.0, server_default="1.0")

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="global_style_profile", uselist=False)


class ContactStyleProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    AI personality style definition for specific contact.
    Ref: Database Design §2.5
    """
    __tablename__ = "contact_style_profile"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    contact_id: Mapped[str] = mapped_column(ForeignKey("contacts.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    style_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    tone_vector: Mapped[list[float] | None] = mapped_column(Vector(1536), nullable=True)
    effective_style_cache: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    # Relationships
    contact: Mapped["Contact"] = relationship("Contact", back_populates="contact_style_profile", uselist=False)

class AgentState(Base, TimestampMixin):
    """
    Active execution state for an agent processing for a user.
    Ref: Database Design §2.10
    """
    __tablename__ = "agent_state"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    
    global_enabled: Mapped[bool] = mapped_column(default=True, server_default="true")
    emergency_stop: Mapped[bool] = mapped_column(default=False, server_default="false")
    session_active: Mapped[bool] = mapped_column(default=False, server_default="false")

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="agent_states", uselist=False)
