import { serve } from "bun";
import {
  ToggleSchema,
  CooldownSchema,
} from "./schemas";

import { parseBody } from "./utils/http";
import {
  getStatus,
  enableSnapshots,
  enableRecording,
  setCooldown,
  getEvents,
} from "./detection";

serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);

    try {
      if (req.method === "GET" && url.pathname === "/status") {
        return Response.json(await getStatus());
      }

      if (req.method === "POST" && url.pathname === "/snapshots") {
        const body = await parseBody(req, ToggleSchema);
        return Response.json(await enableSnapshots(body.enabled));
      }

      if (req.method === "POST" && url.pathname === "/recording") {
        const body = await parseBody(req, ToggleSchema);
        return Response.json(await enableRecording(body.enabled));
      }

      if (req.method === "POST" && url.pathname === "/cooldown") {
        const body = await parseBody(req, CooldownSchema);
        return Response.json(await setCooldown(body.seconds));
      }

      if (req.method === "GET" && url.pathname === "/events") {
        const limit = Number(url.searchParams.get("limit") ?? 20);
        return Response.json(await getEvents(limit));
      }

      return new Response("Not Found", { status: 404 });
    } catch (err: any) {
      return Response.json(
        {
          error: err.message,
        },
        { status: 400 }
      );
    }
  },
});
