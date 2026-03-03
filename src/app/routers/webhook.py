"""
Webhook Router - WhatsApp Webhook Endpoint

Ref: Architecture §3.1, Design §2.2
Endpoint: POST /webhook/whatsapp
"""

from fastapi import APIRouter, Request, Response

router = APIRouter()


@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    """
    Receive incoming WhatsApp webhook events.

    Responsibilities (Architecture §3.1):
    - Validate signature
    - Ensure idempotency
    - Parse payload
    - Enqueue background processing task

    Returns 200 OK immediately to acknowledge receipt.
    """
    # Implementation in Task 11
    return Response(status_code=200)


@router.get("/whatsapp")
async def whatsapp_webhook_verify(request: Request):
    """
    WhatsApp webhook verification challenge endpoint.

    WhatsApp sends a GET request with hub.verify_token
    to verify the webhook URL during setup.
    """
    # Implementation in Task 11
    return Response(status_code=200)
