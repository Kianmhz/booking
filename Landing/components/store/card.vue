<template>
  <div class="flex justify-center items-center flex-col mt-32 md:mt-16">
    <div v-for="(store, storeIndex) in stores" :key="store.id" class="relative grid grid-cols-1 my-24 max-w-4xl w-[90%] md:transform md:my-10 md:translate-x-7 p-10 bg-[--sec-bg] shadow rounded-3xl overflow-visible">
      <div
        v-for="(image, imageIndex) in store.images"
        :key="imageIndex"
        v-show="imageIndex === store.activeImageIndex"
        class="w-full flex flex-col md:flex-row items-center"
      >
        <div class="relative w-full md:w-auto flex justify-center md:justify-start">
          <div class="absolute md:relative top-0 md:top-auto transform -translate-y-1/2 md:transform md:-translate-x-24 md:-translate-y-0 overflow-hidden w-72 h-72 shadow rounded-3xl mb-5 md:mb-0">
            <NuxtImg :src="image" :alt="store.name" class="w-full h-full object-cover" />
          </div>
        </div>
        <div class="flex-1 text-center md:text-left mt-40 md:mt-0">
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
</template>

<script setup>
const stores = ref([
  {
    id: 1,
    name: "Store One",
    images: [
      "https://via.placeholder.com/300",
      "https://via.placeholder.com/300/111",
      "https://via.placeholder.com/300/222"
    ],
    description: "Some quick example text to build on the card title and make up the bulk of the card's content.",
    link: "/store",
    activeImageIndex: 0
  },
  {
    id: 2,
    name: "Store Two",
    images: [
      "https://via.placeholder.com/300",
      "https://via.placeholder.com/300/333",
      "https://via.placeholder.com/300/444"
    ],
    description: "Another example text to showcase the card title and make up the bulk of the card's content.",
    link: "/store",
    activeImageIndex: 0
  },
  {
    id: 3,
    name: "Store Three",
    images: [
      "https://via.placeholder.com/300",
      "https://via.placeholder.com/300/555",
      "https://via.placeholder.com/300/666"
    ],
    description: "More example text to build on the card title and make up the bulk of the card's content.",
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
