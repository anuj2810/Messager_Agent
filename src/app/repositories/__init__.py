"""
Repositories Package - Database Abstraction Layer

Ref: Tech Stack §1.1.5 - Repository Layer (DB abstraction)
Handles all database operations with async queries.

Modules:
  - user_repo: Users CRUD
  - contact_repo: Contacts CRUD
  - message_repo: Messages CRUD
  - conversation_repo: Conversations CRUD
  - style_repo: Style profiles CRUD
  - agent_state_repo: Agent state CRUD (SELECT FOR UPDATE)
  - feedback_repo: Correction feedback CRUD
  - audit_repo: Audit logs CRUD
  - embedding_repo: Message embeddings CRUD
"""
