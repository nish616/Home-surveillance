import cv2
import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
import state

load_dotenv()


def detection_loop():
    try:
        RTSP_URL = os.getenv("RTSP_URL")

        cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        background = None
        last_event_time = 0
        print("Motion detection started")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                continue

            frame = cv2.resize(frame, (640, 360))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)

            if background is None:
                background = gray.astype("float")
                continue

            # Adaptive background
            cv2.accumulateWeighted(gray, background, 0.05)
            delta = cv2.absdiff(gray, cv2.convertScaleAbs(background))
            _, thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)

            motion_pixels = cv2.countNonZero(thresh)
            now = time.time()

            # print(f"Motion pixels: {motion_pixels}")
            # print(f"Snapshots enabled: {state.SNAPSHOT_ENABLED}, Cooldown: {state.COOLDOWN_SECONDS}s")

            if (
                motion_pixels > state.MOTION_PIXEL_MIN_THRESHOLD
                and motion_pixels < state.MOTION_PIXEL_MAX_THRESHOLD
                and now - last_event_time > state.COOLDOWN_SECONDS
            ):
                last_event_time = now

                # Snapshot folder by date
                if state.SNAPSHOT_ENABLED:
                    date_str = datetime.now().strftime("%Y-%m-%d")
                    snapshot_dir = f"snapshots/{date_str}"
                    os.makedirs(snapshot_dir, exist_ok=True)

                    ts = int(now)
                    snapshot_path = f"{snapshot_dir}/{ts}.jpg"

                    cv2.imwrite(snapshot_path, frame)

                    event = {
                        "timestamp": ts,
                        "snapshot": snapshot_path,
                        "motion_pixels": motion_pixels,
                    }

                    os.makedirs("events", exist_ok=True)
                    with open("events/events.jsonl", "a") as f:
                        f.write(json.dumps(event) + "\n")

                    print("📸 Motion event saved:", event)
    finally:
        cap.release()
        print("Motion detection stopped")
