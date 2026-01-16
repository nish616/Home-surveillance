
# Camera Control Service

This service provides an API to control the detection system, such as enabling or disabling snapshots. It is built with Bun (JavaScript runtime).

## Features
- Enable/disable motion detection and snapshots
- Communicate with the Detection Service

## Architecture
See the main repository [architecture diagram](../architecture.puml) for an overview.

## Getting Started


## Environment Variables

Create a `.env` file in this directory with the following variable:

```
ACCESS_TOKEN=<your_authorization_token>
```

- `ACCESS_TOKEN`: The token used to authenticate with the Detection Service. Must match the `ACCESS_TOKEN` set in the Detection Service.

---

### Install dependencies
```bash
bun install
```

### Run the service
```bash
bun run src/index.ts
```

---

## Authorization

When making requests to the Detection Service, this service sends:

```
Authorization: Bearer <ACCESS_TOKEN>
```

Ensure both services use the same token value for successful authorization.

## Project Info
This project was created using `bun init` in bun v1.3.5. [Bun](https://bun.com) is a fast all-in-one JavaScript runtime.
