// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: ['@nuxt/ui-pro'],

  modules: [
    "@nuxt/ui",
    "@nuxtjs/google-fonts",
    "@nuxt/image",
    '@morev/vue-transitions/nuxt',
    'nuxt-aos',
    "@nuxt/fonts",
    '@vueuse/nuxt',
    "@sidebase/nuxt-auth",
  ],

  runtimeConfig: {
    public: {
      apiHost: "http://localhost:3000",
    }
  },

  devtools: { enabled: true },
  css: ["~/assets/main.css",],
  compatibilityDate: "2024-09-12",
});