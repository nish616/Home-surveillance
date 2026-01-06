
# Home Surveillance System

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
