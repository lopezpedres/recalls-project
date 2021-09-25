export type PageProps = {
  is404?: boolean;
};
// The `pageContext` that are available in both on the server-side and browser-side
export type PageContext = {
  Page: (pageProps: PageProps) => string;
  pageProps: PageProps;
  urlPathname: string;
  documentProps?: {
    title?: string;
    description?: string;
  };
};
