from sqlalchemy import Text, ForeignKey, Integer, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Contact(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    """
    Contacts table - Owned by User. Represents individuals communicating with the User.
    Ref: Database Design §2.3
    """
    __tablename__ = "contacts"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    relationship_type_id: Mapped[str | None] = mapped_column(ForeignKey("relationship_types.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="contacts")
    relationship_type: Mapped["RelationshipType"] = relationship("RelationshipType")
    conversations: Mapped[list["Conversation"]] = relationship("Conversation", back_populates="contact")
    contact_style_profile: Mapped["ContactStyleProfile"] = relationship("ContactStyleProfile", back_populates="contact", uselist=False)

class RelationshipType(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Lookup table for relationship types (e.g., formal, friend, family).
    Ref: Database Design §2.2
    """
    __tablename__ = "relationship_types"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
