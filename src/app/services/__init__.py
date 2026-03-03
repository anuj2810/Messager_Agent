"""
Services Package - Business Logic Layer

Ref: Tech Stack §1.1.5 - Service Layer (business logic)
Orchestrates business operations across domain and repository layers.

Modules:
  - message_processor: Full async message processing pipeline (Task 13)
  - agent_state: Agent state management (Task 14)
  - dispatcher: WhatsApp outbound dispatch (Task 15)
  - webhook_security: Webhook signature verification (Task 12)
  - delay_simulator: Human-like response delay (Task 19)
  - logging_service: Structured JSON logging (Task 37)
  - audit_service: Immutable audit logging (Task 38)
  - metrics_service: Metrics collection (Task 39)
"""
