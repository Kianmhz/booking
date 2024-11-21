<script setup>
const activeTab = ref('about');

const changeTab = (tab) => {
    activeTab.value = tab;
};

const services = [{
  title: 'VueUse',
  description: 'Collection of essential Vue Composition Utilities for Vue 2 and 3.',
  to: 'https://github.com/vueuse/vueuse',
  icon: 'i-simple-icons-nuxtdotjs'
}, {
  title: 'ESLint',
  description: 'ESLint module for Nuxt.',
  to: 'https://github.com/nuxt-community/eslint-module',
  icon: 'i-simple-icons-eslint'
}, {
  title: 'Tailwind CSS',
  description: 'Add Tailwind CSS to your Nuxt application in seconds with PurgeCSS included for minimal CSS.',
  to: 'https://github.com/nuxt-modules/tailwindcss',
  icon: 'i-simple-icons-tailwindcss'
}]
</script>

<template>
    <div class="relative flex items-center justify-center mt-16 h-[500px]">
        <div class="absolute inset-0 bg-cover bg-center filter blur-[3px]" style="background-image: url('../assets/img/apple.jpeg')"></div>
        <div class="absolute inset-0 bg-black opacity-50"></div>
        <div class="relative z-10 text-[--text] text-center text-3xl">
            <div>Stanford Store</div>
            <div class="text-xl">Mumbai, India</div>
        </div>
    </div>
    <div class="tabs w-full bg-[--sec-bg] transition duration-300 z-10">
        <UContainer>
            <div class="grid grid-cols-3">
                <button 
                    class="tab-button py-6 lg:py-8 text-sm sm:text-base lg:text-lg border-none cursor-pointer outline-none relative transition-all duration-300"
                    :class="{ 'active': activeTab === 'about' }" @click="changeTab('about')">
                    About
                </button>
                <button 
                    class="tab-button py-6 lg:py-8 text-sm sm:text-base lg:text-lg border-none cursor-pointer outline-none relative transition-all duration-300"
                    :class="{ 'active': activeTab === 'products' }" @click="changeTab('products')">
                    Products
                </button>
                <button 
                    class="tab-button py-6 lg:py-8 text-sm sm:text-base lg:text-lg border-none cursor-pointer outline-none relative transition-all duration-300"
                    :class="{ 'active': activeTab === 'reviews' }" @click="changeTab('reviews')">
                    Reviews
                </button>
            </div>
        </UContainer>
    </div>

    <UContainer>
        <div v-show="activeTab === 'about'">
            <div class="flex flex-col gap-10 my-10">
                <div class="bg-[--sec-bg] p-10 rounded-3xl shadow">
                    <h2 class="text-2xl font-bold mb-4">About Store</h2>
                    <div class="store-description">
                        <p class="text-[--light-text]">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in bibendum velit, at posuere nisi. Sed consequat sem vel elit auctor congue. Proin malesuada arcu nec dolor dignissim, at scelerisque elit posuere.</p>
                    </div>
                    <h2 class="text-2xl font-bold mt-8 mb-4">Location</h2>
                    <div class="store-location">
                        <p class="text-[--light-text]">The store is conveniently located in the heart of Mumbai, India. Its address is 123 Main Street, Mumbai. It is easily accessible and offers a stunning view of the city skyline.</p>
                    </div>
                </div>
                <div class="bg-[--sec-bg] p-10 rounded-3xl shadow">
                    <h2 class="text-2xl font-bold mb-4">Services</h2>
                    <UPageGrid>
                        <UPageCard v-for="(module, index) in services" :key="index" v-bind="module" target="_blank">
                          <template #description>
                            <span class="line-clamp-2">{{ module.description }}</span>
                          </template>
                        </UPageCard>
                    </UPageGrid>
                </div>
                <div>
                    <StoreReview/>
                </div>
            </div>
        </div>
        <div v-show="activeTab === 'products'">
            <div class="container mx-auto px-4 py-6">
                <h2 class="text-2xl font-bold mb-4 text-third-color">Our Products</h2>
                <!-- Products content here -->
            </div>
        </div>
        <div v-show="activeTab === 'reviews'">
            <StoreReviewtab/>
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