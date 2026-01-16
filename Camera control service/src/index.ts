import { serve } from "bun";
import {
  ToggleSchema,
} from "./schemas";

import { parseBody } from "./utils/http";
import {
  enableSnapshots,
} from "./detection";

serve({
  port: 3001,
  async fetch(req) {
    const url = new URL(req.url);

    try {
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
