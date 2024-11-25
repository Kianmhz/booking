<script setup>
definePageMeta({
  layout: 'profile'
});

const config = useRuntimeConfig();
const apiHost = config.public.apiHost;

const profilePage = ref(true);
const storePage = ref(false);
const productsPage = ref(false);
let user = useCookie("user");
let formData = new FormData();

const switchToProfile = () => {
  profilePage.value = true;
  storePage.value = false;
  productsPage.value = false;
};

const switchToStore = () => {
  profilePage.value = false;
  storePage.value = true;
  productsPage.value = false;
};

const switchToProducts = () => {
  profilePage.value = false;
  storePage.value = false;
  productsPage.value = true;
};

const onFileChange = (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = () => {
    formData.set('file', file);
    user.value.imagePreview = reader.result;
  };
  if (file) {
    reader.readAsDataURL(file);
  }
};
</script>

<template>
  <div class="min-h-screen bg-[--sec-bg] mt-16">
    <div class="relative">
      <div class="w-full h-full banner rounded-b-[5%] text-white text-center py-24 w-full"> </div>
      <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 -bottom-25 group">
        <div class="relative w-32 h-32">
          <!-- <NuxtImg
            class="rounded-full w-full h-full border-4 border-white object-cover"
            :src="user.imagePreview || `${apiHost}/uploads/${user.uuid}`"
            alt="Profile Picture"
          /> -->
          <label class="edit-label absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-200 cursor-pointer bg-black bg-opacity-50 text-white text-sm font-semibold rounded-full" for="userImage">
            <span>Change Image</span>
          </label>
          <input
            id="userImage"
            type="file"
            @change="onFileChange"
            class="absolute inset-0 opacity-0 cursor-pointer w-full h-full"
          />
        </div>
      </div>
    </div>
    <div class="mt-20 text-center">
      <!-- <h2 class="text-2xl font-semibold text-[--text]">
        {{ user.first_name }} {{ user.last_name }}
      </h2> -->
    </div>
    <!-- <div class="text-center">
      <h2 class="text-s text-[--light-text]">
        Joined on {{ new Date(user.timestamp * 1000).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric'}) }}
      </h2>
    </div> -->
    <UContainer>
      <div class="p-8 grid grid-cols-1 md:grid-cols-4 gap-x-20 gap-y-10">
        <div class="md:col-span-1 max-sm:text-center">
          <ul class="flex flex-col">
            <li @click="switchToProfile" class="text-lg font-semibold text-[--text] cursor-pointer hover:text-[--main-special] transition-colors duration-200 ease-in-out border-b border-[--border] py-2">Profile</li>
            <li @click="switchToStore" class="text-lg font-semibold text-[--text] cursor-pointer hover:text-[--main-special] transition-colors duration-200 ease-in-out border-[--border] py-2">Store</li>
          </ul>
        </div>
        <div class="md:col-span-3">
          <div v-show="profilePage">
            <ProfileUser />
          </div>
          <div v-show="storePage">
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