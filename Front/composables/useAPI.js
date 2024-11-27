export function useAPI(url, options) {
    return useFetch(url, {
      ...options,
      $fetch: useNuxtApp().$api
    });
}

export function $api(url,options) {
    return useNuxtApp().$api(url,options);
}