import { escapeInject as html, dangerouslySkipEscape } from "vite-plugin-ssr";
import logoUrl from "./favicon.svg";
import type { PageContext } from "../types";
import type { PageContextBuiltIn } from "vite-plugin-ssr/types";
import { createStore } from "lib/store";

export { render };
// See https://vite-plugin-ssr.com/data-fetching
export const passToClient = ["pageProps", "urlPathname"];

async function render(pageContext: PageContextBuiltIn & PageContext) {
  const { Page, pageProps } = pageContext;
  createStore();
  const pageHtml = Page(pageProps);

  // See https://vite-plugin-ssr.com/html-head
  const { documentProps } = pageContext;
  const title = (documentProps && documentProps.title) || "Vite SSR app";
  const desc = (documentProps && documentProps.description) || "App using Vite + vite-plugin-ssr";

  // to inline the CSS on the server side
  // const css = await postcss([tailwindcss(config as any), autoprefixer]).process(style).css;
  // <style>${css}</style>

  const documentHtml = html`<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" href="${logoUrl}" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="${desc}" />

        <title>${title}</title>
      </head>
      <body>
        <div id="page-view">${dangerouslySkipEscape(pageHtml)}</div>
      </body>
    </html>`;

  return {
    documentHtml,
    pageContext: {
      // We can add some `pageContext` here, which is useful if we want to do page redirection https://vite-plugin-ssr.com/page-redirection
    },
  };
}
