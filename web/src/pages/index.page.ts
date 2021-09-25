import { Footer } from "lib/footer";
import { Logo } from "lib/logo";
import { uid } from "lib/utils/uid";
import background from "./background.svg";

export { Page };

function SignupForm() {
  const id = uid();
  if (!import.meta.env.SSR) {
    requestAnimationFrame(() => {
      const form = document.getElementById(id) as HTMLFormElement;
      if (form) {
        // add event listener
        form.addEventListener("submit", (event) => {
          event.preventDefault();
          const formData = new FormData(form);
          const email = formData.get("email");
          window.location.href = `/signin?email=${email}`;
        });
      }
    });
  }
  return /*html*/ `
  <form id="${id}" action="#" class="sm:max-w-xl sm:mx-auto lg:mx-0">
    <div class="sm:flex">
      <div class="min-w-0 flex-1">
        <label for="email" class="sr-only">Email address</label>
        <input name="email" id="email" type="email" placeholder="Enter your email" class="block w-full px-4 py-3 rounded-md border-0 text-base text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-700 focus:ring-offset-brand-500">
      </div>
      <div class="mt-3 sm:mt-0 sm:ml-3">
        <button type="submit" class="block w-full py-3 px-4 rounded-md shadow bg-brand-700 text-white font-medium hover:bg-brand-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-700 focus:ring-offset-brand-500">Sign up</button>
      </div>
    </div>
    <p class="mt-3 text-sm text-black text-opacity-60 sm:mt-4">Sign up for free to continue. By providing your email, you agree to our <a href="#" class="font-medium text-black">terms or service</a>.</p>
  </form>
  `;
}

// landing page
function Page() {
  return /*html*/`
<div class="min-h-screen">
  <div class="relative overflow-hidden">
    <header class="relative">
      <div class="bg-brand-400 pt-6">
        <nav class="relative max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6" aria-label="Global">
          <div class="flex items-center flex-1">
            <div class="flex items-center justify-between w-full md:w-auto">
              <a href="#">
                <span class="sr-only">Workflow</span>
                ${Logo()}
              </a>
              <div class="-mr-2 flex items-center md:hidden">
                <button type="button" class="bg-brand-700 rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-800 focus:outline-none focus:ring-2 focus-ring-inset focus:ring-white" aria-expanded="false">
                  <span class="sr-only">Open main menu</span>
                  <!-- Heroicon name: outline/menu -->
                  <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="hidden space-x-8 md:flex md:ml-10">
              <a href="#" class="text-base font-medium text-black hover:text-opacity-60">Product</a>

              <a href="#" class="text-base font-medium text-black hover:text-opacity-60">Features</a>

              <a href="#" class="text-base font-medium text-black hover:text-opacity-60">Marketplace</a>

              <a href="#" class="text-base font-medium text-black hover:text-opacity-60">Company</a>
            </div>
          </div>
          <div class="hidden md:flex md:items-center md:space-x-6">
            <a href="/signin" class="text-base font-medium text-black hover:text-opacity-60">
              Sign in
            </a>
            <a href="/signin" class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-brand-700 hover:bg-brand-800">
              Sign up
            </a>
          </div>
        </nav>
      </div>

      <!--
        Mobile menu, show/hide based on menu open state.

        Entering: "duration-150 ease-out"
          From: "opacity-0 scale-95"
          To: "opacity-100 scale-100"
        Leaving: "duration-100 ease-in"
          From: "opacity-100 scale-100"
          To: "opacity-0 scale-95"
      -->
      <div class="absolute z-10 top-0 inset-x-0 p-2 transition transform origin-top md:hidden">
        <div class="rounded-lg shadow-md bg-white ring-1 ring-black ring-opacity-5 overflow-hidden">
          <div class="px-5 pt-4 flex items-center justify-between">
            ${Logo()}
            <div class="-mr-2">
              <button type="button" class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-brand-600">
                <span class="sr-only">Close menu</span>
                <!-- Heroicon name: outline/x -->
                <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
          <div class="pt-5 pb-6">
            <div class="px-2 space-y-1">
              <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 hover:bg-gray-50">Product</a>

              <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 hover:bg-gray-50">Features</a>

              <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 hover:bg-gray-50">Marketplace</a>

              <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 hover:bg-gray-50">Company</a>
            </div>
            <div class="mt-6 px-5">
              <a href="/signin" class="block text-center w-full py-3 px-4 rounded-md shadow bg-brand-600 text-white font-medium hover:bg-brand-700">Sign up</a>
            </div>
            <div class="mt-6 px-5">
              <p class="text-center text-base font-medium text-gray-500">Existing customer? <a href="/signin" class="text-gray-900 hover:underline">Login</a></p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <main>
      <div class="pt-10 bg-brand-400 sm:pt-16 lg:pt-8 lg:pb-14 overflow-hidden">
        <div class="mx-auto max-w-7xl lg:px-8">
          <div class="lg:grid lg:grid-cols-2 lg:gap-8">
            <div class="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 sm:text-center lg:px-0 lg:text-left lg:flex lg:items-center">
              <div class="lg:py-24">
                <h1 class="mt-4 text-4xl tracking-tight font-extrabold text-black sm:mt-5 sm:text-6xl lg:mt-6 xl:text-6xl">
                  <span class="block">A better way to</span>
                  <span class="block text-brand-900">manage your supply chain</span>
                </h1>
                <p class="mt-3 text-base text-black text-opacity-60 sm:mt-5 sm:text-xl lg:text-lg xl:text-xl">
                  Put a strong focus on supply chain transparency, traceability and food safety. With this tool, you will be able to do callbacks efficiently, look up records based on a lot code. Reduce waste, optimize cost and lead time by keeping track of your inventory.
                </p>
                <div class="mt-10 sm:mt-12">
                  ${SignupForm()}
                </div>
              </div>
            </div>
            <div class="mt-12 -mb-16 sm:-mb-48 lg:m-0 lg:relative">
              <div class="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 lg:max-w-none lg:px-0">
                <img class="w-full lg:absolute lg:inset-y-0 lg:left-0 lg:h-full lg:w-auto lg:max-w-none" src="${background}" alt="">
              </div>
            </div>
          </div>
        </div>
      </div>

      ${Footer()}
    </main>
  </div>
</div>
  `;
}
