"""
Agent Control Router - Agent State Management Endpoints

Ref: Design §3.1, PRD §8 (User Stories 1-4)
Endpoints:
  POST /agent/toggle          - Global toggle
  POST /agent/contact/{id}/toggle - Per-contact toggle
  POST /agent/kill            - Emergency stop
  POST /agent/review/{id}     - Review mode
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/toggle")
async def toggle_agent():
    """
    Global agent toggle ON/OFF.

    Ref: PRD Story 1, Design §3.1
    - Toggle persists in database
    - Audit log entry created
    """
    # Implementation in Task 29
    return {"status": "not_implemented"}


@router.post("/contact/{contact_id}/toggle")
async def toggle_contact_agent(contact_id: str):
    """
    Per-contact agent toggle.

    Ref: PRD Story 2, Design §3.1
    """
    # Implementation in Task 30
    return {"status": "not_implemented"}


@router.post("/kill")
async def emergency_stop():
    """
    Emergency stop - immediately disables all agent activity.

    Ref: Design §7, Database Design §2.10
    Sets global_enabled=false, emergency_stop=true.
    """
    # Implementation in Task 31
    return {"status": "not_implemented"}


@router.post("/review/{message_id}")
async def review_message(message_id: str):
    """
    Review mode - submit edited message.

    Ref: PRD Story 3, Design §3.1
    """
    # Implementation in Task 32
    return {"status": "not_implemented"}
