import { populate, setupPost } from "./product.ts";

async function main(): Promise<void> {
  const app = document.querySelector("#app")!;

  const m = document.createElement("main");
  await populate(m);
  app.append(m);

  const form = document.querySelector("form")!;
  setupPost(form, () => populate(m));
}

await main();
