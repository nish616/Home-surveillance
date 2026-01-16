import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
import state

load_dotenv()

app = FastAPI(title="Detection Service")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
def toggle_snapshots(body: ToggleRequest, authorization: str = Header(None)):
    print("Received request to toggle snapshots", authorization, ACCESS_TOKEN)
    if authorization != f"Bearer {ACCESS_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    print(f"Setting snapshots enabled to {body.enabled}")
    state.SNAPSHOT_ENABLED = body.enabled
    return {"enabled": state.SNAPSHOT_ENABLED}
