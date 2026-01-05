from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import time
import state

app = FastAPI(title="Detection Service")

class ToggleRequest(BaseModel):
    enabled: bool


class CooldownRequest(BaseModel):
    seconds: int = Field(ge=1, le=300)

class StatusResponse(BaseModel):
    snapshots_enabled: bool
    recording_enabled: bool
    cooldown_seconds: int
    last_event_ts: float | None


class Event(BaseModel):
    timestamp: float
    motion_pixels: int
    snapshot: str | None

@app.post("/snapshots")
def toggle_snapshots(body: ToggleRequest):
    state.snapshots_enabled = body.enabled
    return {"snapshots_enabled": state.snapshots_enabled}

@app.post("/cooldown")
def set_cooldown(body: CooldownRequest):
    state.cooldown_seconds = body.seconds
    return {"cooldown_seconds": state.cooldown_seconds}

@app.get("/events", response_model=list[Event])
def get_events(limit: int = 20):
    return state.events[-limit:]
