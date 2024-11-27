<template>
<UContainer>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10 mt-16 py-10 justify-items-center">
      <!-- {{ propertyList }} -->
      <div v-for="store in propertyList?.results"  class="flex flex-col md:flex-row items-center gap-14 p-8 bg-[--sec-bg] shadow rounded-3xl">
        <div class="overflow-hidden w-72 h-72 shadow rounded-3xl">
          <NuxtImg :src="`/${pickRandomPic()}`" :alt="store.title" class="w-full h-full object-cover" />
        </div>
        <div class="flex-1 text-center md:text-left">
          <div class="text-2xl font-bold text-[--text] mb-4">{{ store.title }}</div>
          <div class="text-[--light-text] mb-6">{{ store.description }}</div>
          <nuxt-link :to="`/property/${store.id}`" class="inline-flex bg-gradient-to-r from-[--main-special] to-[--sec-special] text-white py-3 px-6 rounded-full shadow-lg">Visit Store</nuxt-link>
          </div>
      </div>
    </div>
  </UContainer>
</template>

<script setup>
const exploreStore = useExplore()

const propertyList = await exploreStore.getExplore(1,15)

const randomPics = [
  "cottage.png",
  "cottage2.png",
  "cottage3.png",
  "beach.png",
  "beach2.png",
  "beach3.png",
  "condo.png",
  "condo2.png",
  "condo3.png",
  "mount.png",
  "mount2.png",
  "mount3.png",
]

const pickRandomPic = () => {
  return randomPics[Math.floor(Math.random() * randomPics.length)]
}
</script>
