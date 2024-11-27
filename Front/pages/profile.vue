<script setup>
definePageMeta({
  layout: 'profile'
});


const { data:user } = useAuth()

const profilePage = ref(true);
const propertyPage = ref(false);

const switchToProfile = () => {
  profilePage.value = true;
  propertyPage.value = false;
};

const switchToStore = () => {
  profilePage.value = false;
  propertyPage.value = true;
};
</script>

<template>
  <div class="min-h-screen bg-[--sec-bg] mt-16">
    <div class="relative">
      <div class="w-full h-full banner rounded-b-[5%] text-white text-center py-24"> </div>
    </div>
    <UContainer>
      <div class="p-8 grid grid-cols-1 md:grid-cols-4 gap-x-20 gap-y-10">
        <div class="md:col-span-1 max-sm:text-center">
          <ul class="flex flex-col">
            <li @click="switchToProfile" class="text-lg font-semibold text-[--text] cursor-pointer hover:text-[--main-special] transition-colors duration-200 ease-in-out border-b border-[--border] py-2">Profile</li>
            <li @click="switchToStore" v-if="user.user_type.id == 2" class="text-lg font-semibold text-[--text] cursor-pointer hover:text-[--main-special] transition-colors duration-200 ease-in-out border-[--border] py-2">Properties</li>
          </ul>
        </div>
        <div class="md:col-span-3">
          <div v-show="profilePage">
            <ProfileUser />
          </div>
          <div v-show="propertyPage" v-if="user.user_type.id == 2">
            <ProfileProperty />
          </div>
        </div>
      </div>
    </UContainer>
  </div>
</template>

<style scoped>
  .banner {
    animation: gradient 60s linear infinite alternate;

    background: var(--gradient-color);
    background-size: 1000% 100%;
  }
</style>