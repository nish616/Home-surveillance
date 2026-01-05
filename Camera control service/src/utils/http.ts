import { z } from "zod";

export async function parseBody<T>(
  req: Request,
  schema: z.ZodSchema<T>
): Promise<T> {
  const json = await req.json();
  return schema.parse(json);
}
