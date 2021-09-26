import { classes } from "lib/classes";
import { Logo } from "lib/logo";
import { uid } from "lib/utils/uid";
import { PageProps } from "../../types";

function Nav({class:c, itemClass}: {class?: string, itemClass?: string}) {
  return /*html*/`
    <nav class="${c}">
      <!-- Current: "bg-gray-100 text-gray-900", Default: "text-gray-600 hover:bg-gray-50 hover:text-gray-900" -->
      <a href="/admin" class="${classes(itemClass, "bg-gray-100 text-gray-900 group rounded-md py-2 px-2 flex items-center font-medium")}">
      <!--
        Heroicon name: outline/home

        Current: "text-gray-500", Default: "text-gray-400 group-hover:text-gray-500"
      -->
      <svg class="text-gray-500 mr-4 flex-shrink-0 h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M10 20v-6h4v6h5v-8h3l-10-9 -10 9h3v8h5Z"></path></svg>
      Dashboard
      </a>

      <a href="/admin/users" class="${classes(itemClass, "text-gray-600 hover:bg-gray-50 hover:text-gray-900 group rounded-md py-2 px-2 flex items-center font-medium")}">
      <svg class="text-gray-400 group-hover:text-gray-500 mr-4 flex-shrink-0 h-6 w-6" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16 17v2h-14v-2c0 0 0-4 7-4 7 0 7 4 7 4m-3.5-9.5v0c0-1.933-1.567-3.5-3.5-3.5 -1.933 0-3.5 1.567-3.5 3.5 0 1.933 1.567 3.5 3.5 3.5l-1.5299e-07-3.55271e-15c1.933 8.4494e-08 3.5-1.567 3.5-3.5m3.44 5.5l-4.75292e-08-3.67823e-08c1.24444.96306 1.99869 2.42763 2.06 4v2h4v-2c0 0 0-3.63-6.06-4m-.94-9l6.53122e-09 3.63674e-11c-.688313-.00383272-1.36148.201955-1.93.59l7.8495e-08 1.09676e-07c1.24541 1.74012 1.24541 4.07988-1.62385e-07 5.82l-2.44434e-07-1.6684e-07c.568516.388045 1.24169.593833 1.93.59h-5.01928e-09c1.933 8.4494e-08 3.5-1.567 3.5-3.5 8.4494e-08-1.933-1.567-3.5-3.5-3.5Z" fill="currentColor"></path></svg>
      Users
      </a>
    </nav>
  `;
}

function ProfileDropdown() {
  let open = false;
  const id = uid();
  if (!import.meta.env.SSR) {
    open = window.location.hash === "#profile";
    function onChange(value: boolean) {
      // mutate state
      open = value;
      const menuElement = document.getElementById(`menu-${id}`) as HTMLDivElement;
      if (menuElement) {
        menuElement.classList.toggle("hidden", !open);
      }
    }
    requestAnimationFrame(() => {
      console.log("open", open);
      const button = document.getElementById(id) as HTMLButtonElement;
      button.addEventListener("click", () => {
        console.log("click");
        if (open) {
          window.location.hash = "";
        } else {
          window.location.hash = "#profile";
        }
      });
      window.addEventListener("hashchange", () => {
        if (window.location.hash === "#profile") {
          onChange(true);
        } else {
          onChange(false);
        }
      });
    });
  }
  return /*html*/`
  <!-- Profile dropdown -->
  <div class="ml-3 relative">
  <div>
    <button id="${id}" type="button" class="max-w-xs flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-700" aria-expanded="false" aria-haspopup="true">
      <span class="sr-only">Open user menu</span>
      <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
    </button>
  </div>

  <!--
    Dropdown menu, show/hide based on menu state.

    Entering: "transition ease-out duration-100"
      From: "transform opacity-0 scale-95"
      To: "transform opacity-100 scale-100"
    Leaving: "transition ease-in duration-75"
      From: "transform opacity-100 scale-100"
      To: "transform opacity-0 scale-95"
  -->
  <div id="menu-${id}" class="hidden origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 py-1 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="${id}" tabindex="-1">
    <!-- Active: "bg-gray-100", Not Active: "" -->
    <a href="#" class="block py-2 px-4 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</a>

    <a href="#" class="block py-2 px-4 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-1">Settings</a>

    <a href="#" class="block py-2 px-4 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</a>
  </div>
</div>
  `;
}

export function Layout({children = "", pageProps}: {children?: string, pageProps?: PageProps}) {
  return /*html*/`
<div class="h-screen bg-white overflow-hidden flex">
  <!-- Off-canvas menu for mobile, show/hide based on off-canvas menu state. -->
  <div class="fixed inset-0 z-40 flex md:hidden" role="dialog" aria-modal="true">
    <!--
      Off-canvas menu overlay, show/hide based on off-canvas menu state.

      Entering: "transition-opacity ease-linear duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "transition-opacity ease-linear duration-300"
        From: "opacity-100"
        To: "opacity-0"
    -->
    <div class="fixed inset-0 bg-gray-600 bg-opacity-75" aria-hidden="true"></div>

    <!--
      Off-canvas menu, show/hide based on off-canvas menu state.

      Entering: "transition ease-in-out duration-300 transform"
        From: "-translate-x-full"
        To: "translate-x-0"
      Leaving: "transition ease-in-out duration-300 transform"
        From: "translate-x-0"
        To: "-translate-x-full"
    -->
    <div class="relative max-w-xs w-full bg-white pt-5 pb-4 flex-1 flex flex-col">
      <!--
        Close button, show/hide based on off-canvas menu state.

        Entering: "ease-in-out duration-300"
          From: "opacity-0"
          To: "opacity-100"
        Leaving: "ease-in-out duration-300"
          From: "opacity-100"
          To: "opacity-0"
      -->
      <div class="absolute top-0 right-0 -mr-12 pt-2">
        <button type="button" class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
          <span class="sr-only">Close sidebar</span>
          <!-- Heroicon name: outline/x -->
          <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <div class="flex-shrink-0 px-4 flex items-center">
        ${Logo({class: "hover:text-brand-800 transition-all cursor-pointer"})}
      </div>
      <div class="mt-5 flex-1 h-0 overflow-y-auto">
        ${Nav({ class: "px-2 space-y-1", itemClass: "text-base" })}
      </div>
    </div>

    <div class="flex-shrink-0 w-14">
      <!-- Dummy element to force sidebar to shrink to fit close icon -->
    </div>
  </div>

  <!-- Static sidebar for desktop -->
  <div class="hidden md:flex md:flex-shrink-0">
    <div class="w-64 flex flex-col">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="border-r border-gray-200 pt-5 pb-4 flex flex-col flex-grow overflow-y-auto">
        <div class="flex-shrink-0 px-4 flex items-center">
          ${Logo({class: "hover:text-brand-800 transition-all cursor-pointer"})}
        </div>
        <div class="flex-grow mt-5 flex flex-col">
          ${Nav({ class: "flex-1 bg-white px-2 space-y-1", itemClass: "text-sm" })}
        </div>
      </div>
    </div>
  </div>
  <div class="flex-1 max-w-4xl mx-auto w-0 flex flex-col md:px-8 xl:px-0">
    <div class="relative z-10 flex-shrink-0 h-16 bg-white border-b border-gray-200 flex">
      <button type="button" class="border-r border-gray-200 px-4 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-brand-700 md:hidden">
        <span class="sr-only">Open sidebar</span>
        <!-- Heroicon name: outline/menu-alt-2 -->
        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" />
        </svg>
      </button>
      <div class="flex-1 flex justify-between px-4 md:px-0">
        <div class="flex-1 flex">
          <form class="w-full flex md:ml-0" action="#" method="GET">
            <label for="search-field" class="sr-only">Search</label>
            <div class="relative w-full text-gray-400 focus-within:text-gray-600">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center">
                <!-- Heroicon name: solid/search -->
                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                  <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
                </svg>
              </div>
              <input id="search-field" class="block h-full w-full border-transparent py-2 pl-8 pr-3 text-gray-900 placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-0 focus:border-transparent sm:text-sm" placeholder="Search" type="search" name="search">
            </div>
          </form>
        </div>
        <div class="ml-4 flex items-center md:ml-6">
          <button type="button" class="bg-white p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-700">
            <span class="sr-only">View notifications</span>
            <!-- Heroicon name: outline/bell -->
            <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </button>

          ${ProfileDropdown()}
        </div>
      </div>
    </div>

    <main class="flex-1 relative overflow-y-auto focus:outline-none">
    ${children}
      
    </main>
  </div>
</div>
  `;
}