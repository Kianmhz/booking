<template>
  <div class="bg-[--sec-bg]">
    <!-- Hero section -->
    <div class="hero relative min-h-screen overflow-hidden">
      <div class="hero-bg absolute w-full h-full top-0 left-0"></div>
      <div class="content">
        <UContainer>
          <div class="hero-text">
            <h2 class="uppercase tracking-wider text-lg md:text-xl">Achieving Success, One Milestone at a Time</h2>
            <h1 class="text-5xl sm:text-6xl font-bold my-10">Empowering Your Business Journey</h1>
            <p class="text-xl sm:text-2xl mb-14">Streamline operations, enhance efficiency, and drive growth with Milestone</p>
          </div>
          <div class="hero-btn">
            <UButton
              to="/auth"
              class=" w-full sm:w-auto px-8 py-3 text-lg font-bold rounded-xl transform hover:scale-105"
            >
              Sign Up for Free
            </UButton>
            <p class="mt-4">30 Days free trial · No credit card required</p>
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
                <h2 class="text-3xl leading-8 font-extrabold tracking-tight sm:text-4xl">Empowering</h2>              
                <span class="relative inline-flex sm:inline">
                  <span class="banner blur-lg filter opacity-40 w-full h-full absolute inset-0"></span>
                  <span class="text-3xl leading-8 font-extrabold tracking-tight sm:text-4xl">Store Owners</span>
                </span>
              </div>
              <p class="mt-4 max-w-3xl mx-auto text-center text-xl text-[--light-text]">Milestone provides a comprehensive management app designed to give store owners enhanced business insights, improve customer engagement, automate processes, and mitigate operational risks. Optimize productivity and acknowledge great work effortlessly.</p>
            </div>
            <div class="relative mt-12 lg:mt-24 lg:grid lg:grid-cols-2 lg:gap-8 lg:items-center">
              <div class="relative">
                <h3 class="text-2xl font-extrabold tracking-tight sm:text-3xl">Building Stronger Teams</h3>
                <p class="mt-3 text-lg text-[--light-text]">At Milestone, we focus on creating strong teams by equipping store owners with tools to manage their staff effectively, ensuring they have the necessary experience and skills for success.</p>
                <dl class="mt-10 space-y-10">
                  <ULandingGrid>
                    <ULandingCard v-for="item in transferFeatures" class="col-span-6 row-span-2" icon="i-heroicons-swatch" :title="item.name" description="Choose a primary and a gray color from your Tailwind CSS color palette." />
                  </ULandingGrid>
                </dl>
              </div>
              <div               
              data-aos="fade-left"
              data-aos-offset="300"
              data-aos-duration="1000"
              data-aos-easing="ease-in-out"
              data-aos-once="True" 
              class="mt-10 -mx-4 relative lg:mt-0" aria-hidden="true">
                <svg class="absolute left-1/2 transform -translate-x-1/2 translate-y-16 lg:hidden" width="784" height="404" fill="none" viewBox="0 0 784 404">
                  <defs>
                    <pattern id="ca9667ae-9f92-4be7-abcb-9e3d727f2941" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                      <rect x="0" y="0" width="4" height="4" class="text-gray-200" fill="currentColor" />
                    </pattern>
                  </defs>
                  <rect width="784" height="404" fill="url(#ca9667ae-9f92-4be7-abcb-9e3d727f2941)" />
                </svg>
                <img class="relative mx-auto" width="490" src="https://tailwindui.com/img/features/feature-example-1.png" alt="Feature Image" />
              </div>
            </div>
          </UContainer>

          <svg class="hidden lg:block absolute right-full transform translate-x-1/2 translate-y-12" width="404" height="784" fill="none" viewBox="0 0 404 784" aria-hidden="true">
            <defs>
              <pattern id="64e643ad-2176-4f86-b3d7-f2c5da3b6a6d" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                <rect x="0" y="0" width="4" height="4" class="text-gray-200" fill="currentColor" />
              </pattern>
            </defs>
            <rect width="404" height="784" fill="url(#64e643ad-2176-4f86-b3d7-f2c5da3b6a6d)" />
          </svg>
          
          <UContainer>
            <div class="relative mt-12 sm:mt-16 lg:mt-24">
              <div class="lg:grid lg:grid-flow-row-dense lg:grid-cols-2 lg:gap-8 lg:items-center">
                <div class="lg:col-start-2">
                  <h3 class="text-2xl font-extrabold tracking-tight sm:text-3xl">Leading Management Solutions</h3>
                  <p class="mt-3 text-lg text-[--light-text]">Milestone is a leader in management solutions for store owners. Whether it's inventory management, customer relationship management, or sales analytics, Milestone delivers top-notch solutions tailored to your needs.</p>
                  <dl class="mt-10 space-y-10">
                    <ULandingGrid>
                      <ULandingCard class="col-span-6 row-span-2" icon="i-heroicons-swatch" title="Color Palette" description="Choose a primary and a gray color from your Tailwind CSS color palette." />
                      <ULandingCard class="col-span-6 row-span-4" icon="i-heroicons-wrench-screwdriver" title="Fully Customizable" description="Change the style of any component in your App Config or with ui prop." />
                      <ULandingCard class="col-span-6 row-span-4" icon="i-heroicons-face-smile" title="Icons" description="Choose any of the 100k+ icons from the most popular icon libraries." />
                      <ULandingCard class="col-span-6 row-span-2" icon="i-heroicons-computer-desktop" title="Keyboard Shortcuts" description="Nuxt UI comes with a set of Vue composables to easily handle shortcuts." />
                    </ULandingGrid>
                  </dl>
                </div>
      
                <div               
                data-aos="fade-right"
                data-aos-offset="300"
                data-aos-duration="1000"
                data-aos-easing="ease-in-out"
                data-aos-once="True" 
                class="mt-10 -mx-4 relative lg:mt-0 lg:col-start-1">
                  <svg class="absolute left-1/2 transform -translate-x-1/2 translate-y-16 lg:hidden" width="784" height="404" fill="none" viewBox="0 0 784 404" aria-hidden="true">
                    <defs>
                      <pattern id="e80155a9-dfde-425a-b5ea-1f6fadd20131" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                        <rect x="0" y="0" width="4" height="4" class="text-gray-200" fill="currentColor" />
                      </pattern>
                    </defs>
                    <rect width="784" height="404" fill="url(#e80155a9-dfde-425a-b5ea-1f6fadd20131)" />
                  </svg>
                  <img class="relative mx-auto" width="490" src="https://tailwindui.com/img/features/feature-example-2.png" alt="Management Solutions" />
                </div>
              </div>
            </div>
          </UContainer>
        </div>
      </div>
    </section>

    <!-- Contact Us Section -->
    <UContainer>
      <section class="py-16">
        <div>
          <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
            <div class="banner rounded-lg shadow-xl overflow-hidden lg:grid lg:grid-cols-2 lg:gap-4">
              <div class="pt-10 pb-12 px-6 sm:pt-16 sm:px-16 lg:py-16 lg:pr-0 xl:py-20 xl:px-20">
                <div class="lg:self-center">
                  <h2 class="text-3xl font-extrabold text-white sm:text-4xl">
                    <span class="block">Ready to elevate your business?</span>
                    <span class="block">Start your free trial today.</span>
                  </h2>
                  <p class="mt-4 text-lg leading-6 text-indigo-200">Experience the full power of Milestone and see how we can transform your business operations.</p>
                  <a href="#" class="mt-8 bg-white border border-transparent rounded-md shadow px-5 py-3 inline-flex items-center text-base font-medium text-indigo-600 hover:bg-indigo-50">Sign up for free</a>
                </div>
              </div>
              <div
              data-aos="fade-left"
              data-aos-offset="200"
              data-aos-duration="1000"
              data-aos-easing="ease-in-out"
              data-aos-once="True" 
              class="-mt-6 aspect-w-5 aspect-h-3 md:aspect-w-2 md:aspect-h-1">
                <img class="transform translate-x-6 translate-y-6 rounded-md object-cover object-left-top sm:translate-x-16 lg:translate-y-20" src="https://tailwindui.com/img/component-images/full-width-with-sidebar.jpg" alt="App screenshot" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </UContainer>
  </div>
</template>

<script setup>
const transferFeatures = [
  {
    id: 1,
    name: 'Enhanced Business Insights',
    description:
      'Gain deep insights into your business operations with comprehensive analytics and reporting tools.',
    icon: "line-md:briefcase-twotone",
  },
  {
    id: 2,
    name: 'Customer Engagement',
    description:
      'Improve customer satisfaction and loyalty with tools designed to enhance engagement.',
    icon: "line-md:person-add-twotone",
  },
  {
    id: 3,
    name: 'Automate Processes',
    description:
      'Reduce manual work and increase efficiency with automation features.',
    icon: "line-md:backup-restore",
  },
  {
    id: 4,
    name: 'Operational Risks',
    description:
      'Mitigate operational risks and ensure business continuity with Milestone.',
    icon: "line-md:shield-check-twotone",
  },
]
const communicationFeatures = [
  {
    id: 1,
    name: 'Team Collaboration',
    description:
      'Facilitate effective communication and collaboration among team members.',
    icon: "line-md:laptop-twotone",
  },
  {
    id: 2,
    name: 'Inventory Management',
    description:
      'Keep track of your inventory in real-time and make informed decisions.',
    icon: "line-md:clipboard-check-twotone",
  },
]

onMounted(() => {
  // Initial setup for --stripe-color
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
    #8067e8 10%, /* close to --main-special */
    #9a86f8 15%, /* lighter shade of --main-special */
    #4683f7 20%, /* close to --sec-special */
    #6aa0f8 25%, /* lighter shade of --sec-special */
    #7e65e7 30%  /* a slight variation of --main-special */
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
