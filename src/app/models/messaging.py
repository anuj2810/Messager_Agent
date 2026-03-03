from datetime import datetime, timezone
from sqlalchemy import String, ForeignKey, Integer, Float, Text, JSON, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

from .base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Conversation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Metadata for chat thread linking user and contact.
    Ref: Database Design §2.6
    """
    __tablename__ = "conversations"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    contact_id: Mapped[str] = mapped_column(ForeignKey("contacts.id", ondelete="CASCADE"), nullable=False)
    
    last_message_at: Mapped[datetime | None] = mapped_column(nullable=True)
    summary_id: Mapped[str | None] = mapped_column(ForeignKey("conversation_summaries.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="conversations")
    contact: Mapped["Contact"] = relationship("Contact", back_populates="conversations")
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")
    summary: Mapped["ConversationSummary"] = relationship("ConversationSummary", foreign_keys=[summary_id], back_populates="conversation", uselist=False)


class ConversationSummary(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Summarized context for a conversation thread.
    Ref: Database Design §2.9
    """
    __tablename__ = "conversation_summaries"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    conversation_id: Mapped[str] = mapped_column(ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    summary_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    token_count: Mapped[int] = mapped_column(Integer, default=0, server_default="0")

    # Relationships
    conversation: Mapped["Conversation"] = relationship("Conversation", foreign_keys=[conversation_id], back_populates="summary_list")


class Message(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    """
    Individual chat messages in a conversation.
    Ref: Database Design §2.7
    """
    __tablename__ = "messages"

    tenant_id: Mapped[str] = mapped_column(String(50), nullable=False)
    conversation_id: Mapped[str] = mapped_column(ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    
    message_external_id: Mapped[str | None] = mapped_column(String(255), nullable=True, unique=True)
    direction: Mapped[int] = mapped_column(SmallInteger, nullable=False) # 0 for inbound, 1 for outbound
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    token_count: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    model_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    temperature: Mapped[float | None] = mapped_column(Float, nullable=True)
    latency_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Relationships
    conversation: Mapped["Conversation"] = relationship("Conversation", back_populates="messages")
    embedding: Mapped["MessageEmbedding"] = relationship("MessageEmbedding", back_populates="message", uselist=False, cascade="all, delete-orphan")
    feedback: Mapped["FeedbackCorrection"] = relationship("FeedbackCorrection", back_populates="message", uselist=False)


class MessageEmbedding(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores vector embeddings representing semantics of a given message.
    Ref: Database Design §2.8
    """
    __tablename__ = "message_embeddings"

    message_id: Mapped[str] = mapped_column(ForeignKey("messages.id", ondelete="CASCADE"), nullable=False, unique=True)
    embedding: Mapped[list[float]] = mapped_column(Vector(1536), nullable=False)

    # Relationships
    message: Mapped["Message"] = relationship("Message", back_populates="embedding")
