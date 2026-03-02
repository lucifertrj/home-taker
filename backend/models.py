from typing import Any

from pydantic import BaseModel


class PreferencesRequest(BaseModel):
    userType: str
    preferences: dict[str, Any]
    createdAt: str | None = None


class LogRequest(BaseModel):
    type: str
    title: str
    details: str | None = None


class ChatRequest(BaseModel):
    message: str


class APIResponse(BaseModel):
    success: bool
    message: str
    data: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    response: str
