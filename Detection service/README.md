# Detection Service

This service detects motion using OpenCV and saves snapshots when motion is detected. It can be controlled remotely by the Camera Control Service.

## Features
- Motion detection using OpenCV
- Snapshot storage on motion events
- Receives control commands from Camera Control Service

## Architecture
See the main repository [architecture diagram](../architecture.puml) for an overview.


## Environment Variables

Create a `.env` file in this directory with the following variables:

```
RTSP_URL=rtsp://<user>:<password>@<camera_ip>:<port>/<stream>
```

- `RTSP_URL`: The RTSP stream URL for your camera (including credentials and address).

---

## Getting Started

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the service
```bash
python src/run.py
```

## Project Structure
- `src/` - Source code for detection, event handling, and state management
- `events/` - Event logs
- `snapshots/` - Saved images from motion events

---

For integration, see the Camera Control Service documentation.
