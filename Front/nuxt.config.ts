// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    "@nuxt/ui",
    "@nuxtjs/google-fonts",
    "@nuxt/image",
    '@morev/vue-transitions/nuxt',
    'nuxt-aos',
    "@nuxt/fonts",
    '@vueuse/nuxt',
    "@sidebase/nuxt-auth",
    '@pinia/nuxt',
  ],
  extends: ['@nuxt/ui-pro'],
  app: {
    head: {
        htmlAttrs: { dir: 'ltr', lang: 'en' },
    },
  },
  auth: {
    isEnabled: true,
    globalAppMiddleware: true,
    baseURL: 'http://127.0.0.1:8000/userarea/',
    // baseURL: 'https://api.example.com/userarea/',
    provider: {
      type: 'local',
      pages: {
        login: '/auth',
      },
      token: {
        signInResponseTokenPointer: '/access',
        type: 'Bearer',
        cookieName: 'auth.access',
        headerName: 'Authorization',
        maxAgeInSeconds: 60 * 3,
        sameSiteAttribute: 'lax',
        secureCookieAttribute: false,
        httpOnlyCookieAttribute: false,
      },
      endpoints: {
        signIn: { path: 'login', method: 'POST' },
        signOut: { path: 'logout', method: 'POST' },
        signUp: { path: 'register', method: 'POST' },
        getSession: { path: 'user-info', method: 'GET' },
      },
      refresh: {
        isEnabled:true,
        refreshOnlyToken: true,
        token: {
          signInResponseRefreshTokenPointer: '/refresh',
          refreshRequestTokenPointer: '/refresh',
          cookieName: 'auth.refresh',
          maxAgeInSeconds: 60 * 60 * 24 * 24,
          sameSiteAttribute: 'lax',
          secureCookieAttribute: false,
          httpOnlyCookieAttribute: false,
        },
        endpoint: {
          path: 'refresh',
          method: 'POST',
        },
      },
    },
    sessionRefresh: {
      enablePeriodically: 1000 * 60,
      enableOnWindowFocus: true,
    },
  },
  colorMode: {
    preference: 'system',
    fallback: 'light', // fallback value if not system preference found
  },
  pinia: {
    storesDirs: ['./stores/**'],
  },
  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://127.0.0.1:8000',
      // baseURL: process.env.BASE_URL || 'https://api.example.ccom',
      chunkSize:  5 * 1024 * 1024, // 5MB
    },
  },
  // runtimeConfig: {
  //   public: {
  //     baseURL: "http://localhost:7331"
  //   }
  // },

  devtools: { enabled: true },
  css: ["~/assets/main.css",],
  compatibilityDate: "2024-09-12",
});