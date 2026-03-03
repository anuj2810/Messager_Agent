"""
Domain Package - Core Business Domain Logic

Ref: Tech Stack §1.1.5 - Domain Layer (style logic, tone engine)
Contains pure business logic with no external dependencies.

Modules:
  - prompt_builder: Multi-layer prompt construction (Task 22)
  - context_manager: Token budgeting & context management (Task 23)
  - safety_filter: Output validation & hallucination detection (Task 24)
  - style_engine: Personality trait blending algorithm (Task 25)
  - tone_overlay: Contact-specific tone modifiers (Task 26)
  - emotion_detector: Sentiment classification & de-escalation (Task 27)
  - feedback_learner: Correction diff & trait update learning (Task 28)
  - input_sanitizer: Prompt injection protection (Task 33)
"""
