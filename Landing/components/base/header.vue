<template>
  <header class="fixed bg-[--sec-bg] top-0 w-full z-50 shadow">
    <UContainer>
      <div class="grid grid-flow-col grid-cols-3 h-16">
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
        <div class="hidden sm:flex space-x-10 items-center justify-center col-span-1 font-semibold text-[--text]">
          <nuxt-link class="hover:text-[--main-special] transition-colors duration-300" to="/dashboard">Dashboard</nuxt-link>
          <nuxt-link class="hover:text-[--main-special] transition-colors duration-300" to="/inventory">Inventory</nuxt-link>
          <nuxt-link class="hover:text-[--main-special] transition-colors duration-300" to="/profile">Settings</nuxt-link>
        </div>
        <div class="flex flex-row justify-center md:justify-end items-center col-span-1 space-x-3">
            <UButton
              icon="i-heroicons-magnifying-glass-20-solid"
              color="gray"
              variant="ghost"
              aria-label="Search"
              @click="isOpen = true"
            />
            <UButton
              icon="i-heroicons-arrow-left-on-rectangle-20-solid"
              color="gray"
              variant="ghost"
              aria-label="Login"
              to="/auth"
            />
            <!-- Dark Mode Toggle -->
            <UColorModeButton />
        </div>
        <!-- Mobile Menu Toggle -->
        <BaseMobileMenu />
      </div>
    </UContainer>
    <UModal v-model="isOpen">
      <UCommandPalette ref="commandPaletteRef" :groups="groups" :autoselect="false" @update:model-value="onSelect" />
    </UModal>
  </header>
</template>

<script setup>
const colorMode = useColorMode()
const isOpen = ref(false)
const toast = useToast()
const router = useRouter()
const commandPaletteRef = ref()
const users = [

]

const actions = [
  { id: 'new-file', label: 'Add new file', icon: 'i-heroicons-document-plus', click: () => toast.add({ title: 'New file added!' }), shortcuts: ['⌘', 'N'] },
  { id: 'new-folder', label: 'Add new folder', icon: 'i-heroicons-folder-plus', click: () => toast.add({ title: 'New folder added!' }), shortcuts: ['⌘', 'F'] },
  { id: 'hashtag', label: 'Add hashtag', icon: 'i-heroicons-hashtag', click: () => toast.add({ title: 'Hashtag added!' }), shortcuts: ['⌘', 'H'] },
  { id: 'label', label: 'Add label', icon: 'i-heroicons-tag', click: () => toast.add({ title: 'Label added!' }), shortcuts: ['⌘', 'L'] }
]

const groups = computed(() =>
  [commandPaletteRef.value?.query ? {
    key: 'users',
    commands: users
  } : {
    key: 'recent',
    label: 'Recent searches',
    commands: users.slice(0, 1)
  }, {
    key: 'actions',
    commands: actions
  }].filter(Boolean))
</script>

<style scoped>
.logo {
  font-family: 'Pacifico', cursive;
}
</style>