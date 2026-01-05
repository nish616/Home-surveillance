import threading
import uvicorn
from detect import detection_loop
from app import app

def main():
    # Start detection loop in background thread
    t = threading.Thread(
        target=detection_loop,
        daemon=True
    )
    t.start()

    # Start FastAPI server (blocking)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

if __name__ == "__main__":
    main()
