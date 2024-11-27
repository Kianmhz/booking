<template>
  <header class="fixed bg-[--sec-bg] top-0 w-full z-50 shadow">
    <UContainer>
      <div class="grid grid-flow-col grid-cols-2 h-16">
        <div class="flex items-center space-x-4 col-span-1 justify-start font-bold">
          <nuxt-link to="/" class="flex items-center space-x-2">
            <div class="bg-blue-600 text-white w-12 h-12 flex items-center justify-center text-2xl rounded relative">
              M
              <span class="absolute -bottom-2 -right-2 w-0 h-0 border-l-10 border-r-10 border-b-10 border-r-pink-500 rotate-90"></span>
            </div>
          </nuxt-link>
          <div class="hidden text-2xl sm:block">
            <span class="logo text-[--text] font-Pacifico">Milestone</span>
          </div>
        </div>
        <div class="flex flex-row justify-center md:justify-end items-center col-span-1 space-x-3">
            <UButton
              icon="i-heroicons-magnifying-glass-20-solid"
              color="gray"
              variant="ghost"
              aria-label="Search"
              @click="isOpen = true"
            />
            <UTooltip text="Logout" v-if="user">
              <UButton
                icon="i-heroicons-arrow-left-on-rectangle-20-solid"
                color="gray"
                variant="ghost"
                aria-label="Login"
                to="/logout"
              />
            </UTooltip>

            <UTooltip :text="tooltipProfileText">
              <UButton
                icon="heroicons:user-16-solid"
                color="gray"
                variant="ghost"
                aria-label="Login"
                :to="tooltipProfileLink"
              />
            </UTooltip>

            <!-- Dark Mode Toggle -->
            <UColorModeButton />
        </div>
      </div>
    </UContainer>
    <UModal v-model="isOpen">
      <UCommandPalette ref="commandPaletteRef" :groups="groups" :autoselect="false" @update:model-value="onSelect" />
    </UModal>
  </header>
</template>

<script setup>
const isOpen = ref(false);
const router = useRouter();

const { data:user } = useAuth()

const tooltipProfileText = computed(() => {
  return user.value ? 'Profile' : 'Login';
});

const tooltipProfileLink = computed(() => {
  return user.value ? '/profile' : '/auth';
});

const actions = [
  {
    id: 'go-home',
    label: 'Home',
    icon: 'i-heroicons-home',
    click: () => router.push('/')
  },
  {
    id: 'go-explore',
    label: 'Explore',
    icon: 'heroicons:globe-alt',
    click: () => router.push('/explore')
  }
];

const groups = computed(() => [
  {
    key: 'actions',
    label: 'Actions',
    commands: actions
  }
]);

const onSelect = (command) => {
  if (command?.click) {
    command.click();
  } else {
    console.warn('No action defined for this command:', command);
  }
};
</script>


<style scoped>
.logo {
  font-family: 'Pacifico', cursive;
}
</style>