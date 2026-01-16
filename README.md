

# Home Surveillance System


## Background

This project is a modular enhancement to traditional home surveillance systems, introducing automated motion-based snapshot capture—a feature not commonly available with most commercial camera service providers. With this open-source solution, anyone can freely upgrade their surveillance setup to automatically save images whenever motion is detected, without vendor lock-in or subscription fees.

It consists of two main services:
- **Camera Control Service (Bun):** Acts as the central controller, allowing users to enable or disable motion-based snapshot recording and manage detection settings through a simple API or frontend.
- **Detection Service (OpenCV/Python):** Continuously monitors video streams for motion events and saves snapshots when activity is detected, based on the configuration received from the control service.

**How it's helpful:**
- Empowers users to enhance their surveillance capabilities for free.
	- Most automated surveillance capabilities require subscriptions even for very basic use cases. With this project, anyone with basic CS knowledge can enhance their home surveillance for free.
**About RTSP:**
This project leverages the Real Time Streaming Protocol (RTSP), a standard protocol supported by most IP cameras, to access live video streams. By connecting to your camera's RTSP stream, the Detection Service can process video in real time, detect motion, and trigger snapshot captures automatically. This means you can use virtually any RTSP-enabled camera, regardless of brand, and benefit from advanced motion-based recording features.


## Architecture Diagram

This project consists of two main services:

- **Camera Control Service (Bun):** Controls detection and enables/disables snapshots.
- **Detection Service (OpenCV/Python):** Detects motion and saves snapshots.

The following diagram illustrates the architecture:



```
	+---------------------+         +----------------------+
	|  User (API/Frontend)|         |  Detection Service   |
	+---------------------+         |   (OpenCV/Python)    |
			  |                     +----------------------+
			  |                             ^
			  v                             |
	+---------------------+         +----------------------+
	| Camera Control      |-------->|  (Config/Control)    |
	| Service (Bun)       |         |                      |
	+---------------------+         +----------------------+
```

---

See each service's folder for setup and usage instructions.
