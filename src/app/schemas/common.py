"""
Common Schemas - Shared Pydantic Models

Ref: Design §3.2 - Standard Error Model
Ref: Security §9 - Pydantic schema validation, strict JSON parsing
"""

from pydantic import BaseModel, ConfigDict


class ErrorDetail(BaseModel):
    """Standard error response model. Ref: Design §3.2"""
    model_config = ConfigDict(strict=True)

    code: str
    message: str
    trace_id: str
    retryable: bool = False


class ErrorResponse(BaseModel):
    """Wrapper for error responses."""
    error: ErrorDetail


class StatusResponse(BaseModel):
    """Generic status response."""
    status: str
    message: str | None = None
