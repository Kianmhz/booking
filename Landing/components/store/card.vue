<template>
  <UContainer>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10 mt-16 py-10 justify-items-center">
      <div v-for="(store, storeIndex) in stores" :key="store.id" class="relative p-8 bg-[--sec-bg] shadow rounded-3xl">
        <div
          v-for="(image, imageIndex) in store.images"
          :key="imageIndex"
          v-show="imageIndex === store.activeImageIndex"
          class="flex flex-col md:flex-row items-center gap-10"
        >
          <div class="overflow-hidden w-72 h-72 shadow rounded-3xl">
            <NuxtImg :src="image" :alt="store.name" class="w-full h-full object-cover" />
          </div>
          <div class="flex-1 text-center md:text-left">
            <div class="text-2xl font-bold text-[--text] mb-4">{{ store.name }}</div>
            <div class="text-[--light-text] mb-6">{{ store.description }}</div>
            <nuxt-link :to="store.link" class="inline-flex bg-gradient-to-r from-[--main-special] to-[--sec-special] text-white py-3 px-6 rounded-full shadow-lg">Visit Store</nuxt-link>
          </div>
        </div>
        <div class="absolute z-20 right-5 md:top-1/2 md:transform md:-translate-y-1/2 flex md:flex-col space-x-2 md:space-x-0 md:space-y-2 bottom-4 md:bottom-auto md:right-4">
          <span
            v-for="(image, imageIndex) in store.images"
            :key="imageIndex"
            class="w-3 h-3 rounded-full bg-[--main-bg] transition-opacity duration-300 cursor-pointer"
            :class="{ 'bg-[--main-special]': imageIndex === store.activeImageIndex }"
            @click="setActive(storeIndex, imageIndex)"
          ></span>
        </div>
      </div>
    </div>    
  </UContainer>
</template>

<script setup>
const stores = ref([
  {
    id: 1,
    name: "Cozy Cottage",
    images: [
      "cottage.png",
      "cottage2.png",
      "cottage3.png",
    ],
    description: "A cozy cottage in the woods.",
    link: "/store",
    activeImageIndex: 0
  },
  {
    id: 2,
    name: "Beachfront Villa",
    images: [
      "beach.png",
      "beach2.png",
      "beach3.png",
    ],
    description: "A beautiful villa by the beach.",
    link: "/store",
    activeImageIndex: 0
  },
  {
    id: 3,
    name: "City Apartment",
    images: [
      "condo.png",
      "condo2.png",
      "condo3.png",
    ],
    description: "An apartment in the heart of the city.",
    link: "/store",
    activeImageIndex: 0
  },
  {
    id: 4,
    name: "Mountain Lodge",
    images: [
      "mount.png",
      "mount2.png",
      "mount3.png",
    ],
    description: "A lodge with stunning mountain views.",
    link: "/store",
    activeImageIndex: 0
  }
]);

const setActive = (storeIndex, imageIndex) => {
  stores.value[storeIndex].activeImageIndex = imageIndex;
};

const nextSlide = (storeIndex) => {
  const store = stores.value[storeIndex];
  store.activeImageIndex = (store.activeImageIndex + 1) % store.images.length;
};

onMounted(() => {
  setInterval(() => {
    stores.value.forEach((store, index) => {
      nextSlide(index);
    });
  }, 5000);
});
</script>
