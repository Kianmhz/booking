<template>
  <footer class="w-full bg-[--sec-bg]">
    <div class="border-y border-[--border] py-8">
      <UContainer>
        <div class="grid mb-4 md:grid-cols-4 gap-10">
          <div class="flex flex-col">
            <span class="pb-5 text-[--text] font-bold">Company</span>
            <nuxt-link class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300" to="/about">About Us</nuxt-link>
            <nuxt-link class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300">Privacy Policy</nuxt-link>
            <nuxt-link class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300">Terms of Service</nuxt-link>
          </div>
          <div class="flex flex-col">
            <span class="pb-5 text-[--text] font-bold">Support</span>
            <nuxt-link class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300" to="/help">Help Center</nuxt-link>
            <nuxt-link class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300" to="/system">System Status</nuxt-link>
          </div>
          <div class="flex flex-col">
            <span class="pb-5 text-[--text] font-bold">Social</span>
            <a href="#" class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300">Instagram</a>
            <a href="#" class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300">X / Twitter</a>
            <a href="#" class="pb-2 text-[--text] hover:text-[--main-special] transition-colors duration-300">WhatsApp</a>
          </div>
          <div class="flex flex-col">
            <span class="pb-5 text-[--text] font-bold">About Milestone</span>
            <p class="text-[--text]">Milestone is dedicated to helping store owners streamline their operations, manage inventory efficiently, and enhance customer engagement.</p>
          </div>
        </div>
      </UContainer>
    </div>
    <div class="py-4 bg-[--sec-bg]">
      <UContainer>
        <div class="flex flex-wrap justify-between items-center text-sm text-[--text]">
          <div class="flex flex-wrap items-center space-x-4">
            <p>&copy; 2024 Ærvin & Kianmhz. All rights reserved.</p>
            <nuxt-link class="hover:text-[--main-special] transition-colors duration-300">Privacy</nuxt-link>
            <nuxt-link class="hover:text-[--main-special] transition-colors duration-300">Terms</nuxt-link>
          </div>
          <div class="flex space-x-4 text-[--text] text-lg mt-4 sm:mt-0">
            <Icon name="mdi:instagram" size="20" class="hover:text-[--main-special] transition-colors duration-300"/>
            <Icon name="fa6-brands:x-twitter" size="20" class="hover:text-[--main-special] transition-colors duration-300" />
            <Icon name="ic:baseline-whatsapp" size="20" class="hover:text-[--main-special] transition-colors duration-300"/>
          </div>
        </div>
      </UContainer>
    </div>
  </footer>
</template>