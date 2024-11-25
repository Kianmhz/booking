<template>
  <div class="bg-[--sec-bg]">
    <!-- Hero Section -->
    <div class="hero relative min-h-screen overflow-hidden">
      <div class="hero-bg absolute w-full h-full top-0 left-0"></div>
      <div class="content">
        <UContainer>
          <div class="hero-text">
            <h2 class="uppercase tracking-wider text-lg md:text-xl">Your Perfect Stay, One Milestone Away</h2>
            <h1 class="text-5xl sm:text-6xl font-bold my-10">Empowering Your Travel Experience</h1>
            <p class="text-xl sm:text-2xl mb-14">Find the perfect stay, create unforgettable memories, and explore with Milestone</p>
          </div>
          <div class="hero-btn">
            <UButton
              to="/explore"
              class="w-full sm:w-auto px-8 py-3 text-lg font-bold rounded-xl"
            >
              Start Exploring
            </UButton>
          </div>
        </UContainer>
      </div>
    </div>

    <!-- Features Section -->
    <section class="py-16">
      <div class="overflow-hidden lg:py-24">
        <div class="relative max-w-xl mx-auto lg:max-w-7xl">
          <svg class="hidden lg:block absolute left-full transform -translate-x-1/2 -translate-y-1/4" width="404" height="784" fill="none" viewBox="0 0 404 784" aria-hidden="true">
            <defs>
              <pattern id="b1e6e422-73f8-40a6-b5d9-c8586e37e0e7" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                <rect x="0" y="0" width="4" height="4" class="text-gray-200" fill="currentColor" />
              </pattern>
            </defs>
            <rect width="404" height="784" fill="url(#b1e6e422-73f8-40a6-b5d9-c8586e37e0e7)" />
          </svg>
          <UContainer>
            <div class="relative">
              <div class="flex justify-center items-center gap-4">
                <h2 class="text-3xl leading-8 font-extrabold tracking-tight sm:text-4xl">Redefining</h2>              
                <span class="relative inline-flex sm:inline">
                  <span class="banner blur-lg filter opacity-40 w-full h-full absolute inset-0"></span>
                  <span class="text-3xl leading-8 font-extrabold tracking-tight sm:text-4xl">Travel Comfort</span>
                </span>
              </div>
              <p class="mt-4 max-w-3xl mx-auto text-center text-xl text-[--light-text]">Milestone connects travelers with extraordinary stays. Discover destinations tailored to your needs, and enjoy seamless booking experiences.</p>
            </div>
            <div class="relative mt-12 lg:mt-24 lg:grid lg:grid-cols-2 lg:gap-8 lg:items-center">
              <div class="relative">
                <h3 class="text-2xl font-extrabold tracking-tight sm:text-3xl">Personalized Stays</h3>
                <p class="mt-3 text-lg text-[--light-text]">Curate your stay experience with tailored recommendations and top-notch amenities to fit your travel style.</p>
                <dl class="mt-10 space-y-10">
                  <ULandingGrid>
                    <ULandingCard v-for="item in travelFeatures" class="col-span-6 row-span-2" :icon="item.icon" :title="item.name" :description="item.description" />
                  </ULandingGrid>
                </dl>
              </div>
              <div               
              data-aos="fade-left"
              data-aos-offset="300"
              data-aos-duration="1000"
              data-aos-easing="ease-in-out"
              data-aos-once="true" 
              class="mt-10 -mx-4 relative lg:mt-0" aria-hidden="true">
                <NuxtImg class="shadow relative mx-auto" width="490" src="feature.png" alt="Feature Image" />
              </div>
            </div>
          </UContainer>
        </div>
      </div>
    </section>

    <UContainer>
      <section class="py-16">
        <div>
          <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
            <div class="banner rounded-lg shadow-xl overflow-hidden lg:grid lg:grid-cols-2 lg:gap-4">
              <div class="pt-10 pb-12 px-6 sm:pt-16 sm:px-16 lg:py-16 lg:pr-0 xl:py-20 xl:px-20">
                <div class="lg:self-center">
                  <h2 class="text-3xl font-extrabold text-white sm:text-4xl">
                    <span class="block">Ready for your next adventure?</span>
                    <span class="block">Discover your Milestone today.</span>
                  </h2>
                  <p class="mt-4 text-lg leading-6 text-indigo-200">Experience the full potential of Milestone and start exploring the best stays and unique destinations.</p>
                  <nuxt-link to="/explore" class="mt-8 bg-white border border-transparent rounded-md shadow px-5 py-3 inline-flex items-center text-base font-medium text-indigo-600 hover:bg-indigo-50">Start Exploring</nuxt-link>
                </div>
              </div>
              <div
              data-aos="fade-left"
              data-aos-offset="200"
              data-aos-duration="1000"
              data-aos-easing="ease-in-out"
              data-aos-once="true" 
              class="-mt-6 aspect-w-5 aspect-h-3 md:aspect-w-2 md:aspect-h-1">
                <NuxtImg class="transform translate-x-6 translate-y-6 rounded-md object-cover object-left-top sm:translate-x-16 lg:translate-y-20" src="app.png" alt="App screenshot" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </UContainer>
  </div>
</template>

<script setup>
definePageMeta({
  colorMode: 'light',
})


const travelFeatures = [
  {
    id: 1,
    name: 'Personalized Stays',
    description: 'Curate your stay experience with tailored recommendations.',
    icon: "material-symbols:hotel-outline",
  },
  {
    id: 2,
    name: 'Seamless Booking',
    description: 'Effortlessly reserve your dream stay.',
    icon: "line-md:backup-restore",
  },
  {
    id: 3,
    name: 'Verified Hosts',
    description: 'Stay confidently with our verified listings.',
    icon: "tabler:shield-check",
  },
  {
    id: 4,
    name: 'Guest Reviews',
    description: 'Make informed decisions with genuine feedback.',
    icon: "ic:baseline-person-add-alt",
  },
]

onMounted(() => {
  document.documentElement.style.setProperty('--stripe-color', '#fff');
});
</script>

<style scoped>
.hero {
  min-height: 100vh;
}

.hero-bg {
  --stripes: repeating-linear-gradient(
    100deg,
    var(--stripe-color) 0%,
    var(--stripe-color) 7%,
    transparent 10%,
    transparent 12%,
    var(--stripe-color) 16%
  );

  --rainbow: repeating-linear-gradient(
    100deg,
    #8067e8 10%,
    #9a86f8 15%,
    #4683f7 20%,
    #6aa0f8 25%,
    #7e65e7 30%
  );
  background-image: var(--stripes), var(--rainbow);
  background-size: 300%, 200%;
  background-position: 50% 50%, 50% 50%;
  filter: blur(10px) invert(100%);
  mask-image: radial-gradient(ellipse at 100% 0%, black 40%, transparent 70%);
}

.hero-bg::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--stripes), var(--rainbow);
  background-size: 200%, 100%;
  animation: smoothBg 60s linear infinite;
  background-attachment: fixed;
  mix-blend-mode: difference;
}

.content {
  position: absolute;
  inset: 0;
  place-content: center;
  text-align: center;
  mix-blend-mode: difference;
  -webbkit-mix-blend-mode: difference;
  filter: invert(1);
}

.hero-text {
  animation: FadeAnimation 1s ease-in-out;
}

.hero-btn {
  opacity: 0;
  animation: FadeAnimation 1s ease-in-out 1.5s forwards;
}
</style>