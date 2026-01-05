import { serve } from "bun";
import {
  ToggleSchema,
  CooldownSchema,
} from "./schemas";

import { parseBody } from "./utils/http";
import {
  getStatus,
  enableSnapshots,
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
