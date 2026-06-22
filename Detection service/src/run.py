import threading
import uvicorn
import os
from detect import detection_loop
from app import app
from camera import Camera
def main():

    front_cam = Camera(
        os.getenv("RTSP_USERNAME"),
        os.getenv("RTSP_PASSWORD"),
        os.getenv("RTSP_IP"),
        os.getenv("RTSP_PORT")
    )

    front_cam_url = front_cam.generate_rtsp_url()

    threading.Thread(
        target=detection_loop,
        args=(front_cam_url,),
        daemon=True
    ).start()

    # Start FastAPI server (blocking)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

if __name__ == "__main__":
    main()
