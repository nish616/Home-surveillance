import os
import time
from datetime import datetime

import cv2


CLIP_DURATION_SECONDS = 5
# Target FPS for the output container. Real frame rate from RTSP varies;
# if the camera delivers fewer/more fps than this, playback will be
# slightly slower/faster than real-time. 15 is a typical stream2 rate.
CLIP_FPS = 15.0


def record_clip(cap: cv2.VideoCapture, timestamp: int) -> str | None:
    """Record a clip from the already-open OpenCV capture.

    This uses the SAME RTSP connection as the detection loop — no second
    connection to the camera — but it blocks the caller for
    CLIP_DURATION_SECONDS. That's fine here because the detect loop has a
    cooldown longer than CLIP_DURATION_SECONDS, so nothing useful is missed.

    Returns the output path, or None on failure.
    """
    if cap is None or not cap.isOpened():
        return None

    date_str = datetime.now().strftime("%Y-%m-%d")
    clip_dir = f"clips/{date_str}"
    os.makedirs(clip_dir, exist_ok=True)
    clip_path = f"{clip_dir}/{timestamp}.mp4"

    # Read a sample frame to learn dimensions before opening the writer.
    ret, sample = cap.read()
    if not ret or sample is None:
        print("recorder: failed to read sample frame")
        return None

    h, w = sample.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(clip_path, fourcc, CLIP_FPS, (w, h))
    if not writer.isOpened():
        print("recorder: VideoWriter failed to open")
        return None

    try:
        writer.write(sample)
        start = time.time()
        frames = 1
        while time.time() - start < CLIP_DURATION_SECONDS:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue
            writer.write(frame)
            frames += 1
        print(f"recorder: wrote {frames} frames to {clip_path}")
        return clip_path
    finally:
        writer.release()
