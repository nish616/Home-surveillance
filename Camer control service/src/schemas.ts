import { z } from "zod";

// ---------- CONTROL ----------

export const ToggleSchema = z.object({
  enabled: z.boolean(),
});

export const CooldownSchema = z.object({
  seconds: z
    .number()
    .int()
    .min(1)
    .max(300),
});

// ---------- RESPONSES ----------

export const StatusSchema = z.object({
  snapshots_enabled: z.boolean(),
  recording_enabled: z.boolean(),
  cooldown_seconds: z.number(),
  last_event_ts: z.number().nullable(),
});

export const EventSchema = z.object({
  timestamp: z.number(),
  snapshot: z.string(),
  motion_pixels: z.number(),
});

export const EventsSchema = z.object({
  events: z.array(EventSchema),
});
