import { getPage } from "vite-plugin-ssr/client";
import type { PageContext } from "../types";
import type { PageContextBuiltInClient } from "vite-plugin-ssr/types";
import "./style.css";
import { createStore } from "lib/store";

hydrate();

async function hydrate() {
  // For Client Routing we should use `useClientRouter()` instead of `getPage()`.
  // See https://vite-plugin-ssr.com/useClientRouter
  const pageContext = await getPage<PageContextBuiltInClient & PageContext>();
  const { Page, pageProps } = pageContext;

  createStore();

  const app = document.getElementById("page-view");
  if (app && Page) {
    app.innerHTML = Page(pageProps);
  }
}
