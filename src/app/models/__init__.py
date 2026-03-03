"""
Database ORM Models Registry

Centralized import for all SQLAlchemy 2.0 ORM models, ensuring they are loaded
prior to Alembic or standard `Base.metadata.create_all()` calls.

Ref: Database Design §2 - Logical Schema Design
"""

from .base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin
from .users import User
from .contacts import Contact, RelationshipType

from .ai_profiles import (
    UserGlobalStyleProfile,
    ContactStyleProfile,
    AgentState
)

from .messaging import (
    Conversation,
    ConversationSummary,
    Message,
    MessageEmbedding
)

from .operational import (
    FeedbackCorrection,
    AuditLog,
    SystemConfig
)

# Explicitly exposing for external module usage
__all__ = [
    "Base",
    "UUIDPrimaryKeyMixin",
    "TimestampMixin",
    "SoftDeleteMixin",
    "User",
    "Contact",
    "RelationshipType",
    "UserGlobalStyleProfile",
    "ContactStyleProfile",
    "AgentState",
    "Conversation",
    "ConversationSummary",
    "Message",
    "MessageEmbedding",
    "FeedbackCorrection",
    "AuditLog",
    "SystemConfig"
]
