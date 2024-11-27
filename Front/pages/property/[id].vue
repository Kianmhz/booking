<script setup>
definePageMeta({
    auth: false,
})

const route = useRoute()
const { id } = route.params
const exploreStore = useExplore()


definePageMeta({
    validate: async (route) => {
        const { id } = route.params;
        if (isNaN(id)) return false;
		return true;
	},
})

const res = await exploreStore.getSingleExplore(id)

const activeTab = ref('about');

const changeTab = (tab) => {
    activeTab.value = tab;
};

const services = [{
  title: 'WIFI',
  to: '#',
  icon: 'heroicons:wifi-16-solid'
}, {
  title: 'Parking',
  to: '#',
  icon: 'material-symbols:local-parking-rounded'
}, {
  title: 'Swimming Pool',
  to: '#',
  icon: 'material-symbols:pool'
}]

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

<template>
    <div class="relative flex items-center justify-center mt-16 h-[500px]">
        <NuxtImg :src="`/${pickRandomPic()}`" class="absolute inset-0 w-full h-full object-cover filter blur-[3px]"></NuxtImg>
        <div class="absolute inset-0 bg-black opacity-50"></div>
        <div class="relative z-10 text-[#EEEEEE] text-center text-3xl">
            <div>{{ res.title }}</div>
        </div>
    </div>
    <div class="tabs w-full bg-[--sec-bg] transition duration-300 z-10">
        <UContainer>
            <div class="grid grid-cols-2">
                <button
                    class="tab-button py-6 lg:py-8 text-sm sm:text-base lg:text-lg border-none cursor-pointer outline-none relative transition-all duration-300"
                    :class="{ 'active': activeTab === 'about' }" @click="changeTab('about')">
                    About
                </button>
                <button
                    class="tab-button py-6 lg:py-8 text-sm sm:text-base lg:text-lg border-none cursor-pointer outline-none relative transition-all duration-300"
                    :class="{ 'active': activeTab === 'booking' }" @click="changeTab('booking')">
                    Booking
                </button>
            </div>
        </UContainer>
    </div>

    <UContainer>
        <div v-show="activeTab === 'about'">
            <div class="flex flex-col gap-10 my-10">
                <div class="bg-[--sec-bg] p-10 rounded-3xl shadow">
                    <h2 class="text-2xl font-bold mb-4">About Property</h2>
                    <div class="store-description">
                        <p class="text-[--light-text]">{{ res.description }}</p>
                    </div>
                    <h2 class="text-2xl font-bold mt-8 mb-4">Location</h2>
                    <div class="store-location">
                        <p class="text-[--light-text]">{{ res.location }}</p>
                    </div>
                </div>
                <div class="bg-[--sec-bg] p-10 rounded-3xl shadow">
                    <h2 class="text-2xl font-bold mb-4">Amenities</h2>
                    <UPageGrid>
                        <UPageCard v-for="(module, index) in services" :key="index" v-bind="module" target="_blank">
                          <template #description>
                            <span class="line-clamp-2">{{ module.description }}</span>
                          </template>
                        </UPageCard>
                    </UPageGrid>
                </div>
                <div>
                    <PropertyReview :id="id"/>
                </div>
            </div>
        </div>
        <div v-show="activeTab === 'booking'">
            <PropertyBooking :id="id"/>
        </div>
    </UContainer>
</template>

<style scoped>
.tab-button::after {
    content: '';
    display: block;
    height: 3px;
    width: 100%;
    background-color: var(--text);
    transition: all 0.3s ease-in-out;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%) scaleX(0);
}

.tab-button:hover {
    background: var(--border);
}

.tab-button.active::after {
    transform: translateX(-50%) scaleX(1);
}
</style>