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
  ],

  runtimeConfig: {
    public: {
      apiHost: "http://localhost:7331"
    }
  },

  devtools: { enabled: true },
  css: ["~/assets/main.css",],
  compatibilityDate: "2024-09-12",
});