import { z } from "zod";
import {
  StatusSchema,
  ToggleSchema,
  CooldownSchema,
  EventSchema,
} from "./schemas";

const BASE_URL = "http://localhost:8000";

async function request<T>(
  path: string,
  schema: z.ZodSchema<T>,
  options: RequestInit = {}
): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Detection service error ${res.status}: ${text}`);
  }

  return schema.parse(await res.json());
}

// -------- STATUS --------

export function getStatus() {
  return request("/status", StatusSchema);
}

// -------- CONTROLS --------

export function enableSnapshots(enabled: boolean) {
  return request("/control/snapshots", ToggleSchema, {
    method: "POST",
    body: JSON.stringify({ enabled }),
    headers: {
      "Content-Type": "application/json",
      "authorization": `Bearer ${process.env.ACCESS_TOKEN}`,
    },
  });
}

export function setCooldown(seconds: number) {
  return request("/control/cooldown", CooldownSchema, {
    method: "POST",
    body: JSON.stringify({ seconds }),
  });
}
