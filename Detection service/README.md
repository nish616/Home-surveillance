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
ACCESS_TOKEN=<your_authorization_token>
```

- `RTSP_URL`: The RTSP stream URL for your camera (including credentials and address).
- `ACCESS_TOKEN`: Secret token required for authorized API requests (used in the `Authorization` header as `Bearer <ACCESS_TOKEN>`).

---

## Getting Started


## Running with Docker

### Build the Docker image
```bash
docker build -t detection-service .
```

### Run with Docker Compose
1. Ensure your `.env` file is set up as described above.
2. Start the service:
```bash
docker-compose up -d
```

The service will be available on port 8000. Snapshots and events will be stored in the `snapshots/` and `events/` folders, respectively, and are mapped as volumes.

---

## Local Development (without Docker)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the service
```bash
python src/run.py
```

---

## Authorization

All control API endpoints require an `Authorization` header:

```
Authorization: Bearer <ACCESS_TOKEN>
```

Requests without the correct token will be rejected with a 401 Unauthorized error.

## Project Structure
- `src/` - Source code for detection, event handling, and state management
- `events/` - Event logs
- `snapshots/` - Saved images from motion events

---

For integration, see the Camera Control Service documentation.
