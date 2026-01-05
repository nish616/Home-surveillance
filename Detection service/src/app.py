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

@app.post("/control/snapshots")
def toggle_snapshots(body: ToggleRequest):
    print(f"Setting snapshots enabled to {body.enabled}")
    state.SNAPSHOT_ENABLED = body.enabled
    return {"enabled": state.SNAPSHOT_ENABLED}
