<template>
    <div class="relative flex flex-row justify-end items-center col-span-1 sm:hidden">
        <input type="checkbox" id="menu-toggle" class="absolute w-10 h-10 top-0 right-0 opacity-0 cursor-pointer z-10"/>
        <label for="menu-toggle" class="flex flex-col justify-between w-8 h-6 z-20 cursor-pointer">
          <span class="block w-8 h-1 bg-[--text] rounded transition-transform duration-500 ease-in-out"></span>
          <span class="block w-8 h-1 bg-[--text] rounded transition-opacity duration-500 ease-in-out"></span>
          <span class="block w-8 h-1 bg-[--text] rounded transition-transform duration-500 ease-in-out"></span>
        </label>
        <ul id="menu" class="fixed left-0 top-16 w-full h-[calc(100%-4rem)] bg-[--sec-bg] flex flex-col justify-center items-center transform translate-x-full transition-transform duration-500 ease-in-out z-40">
          <li class="py-2 text-2xl"><nuxt-link to="/dashboard" class="hover:text-[--link-hover]">Dashboard</nuxt-link></li>
          <li class="py-2 text-2xl"><nuxt-link to="/inventory" class="hover:text-[--link-hover]">Inventory</nuxt-link></li>
          <li class="py-2 text-2xl"><nuxt-link to="/profile" class="hover:text-[--link-hover]">Settings</nuxt-link></li>
        </ul>
    </div>
</template>

<style scoped>
    input:checked ~ #menu {
    transform: translateX(0);
    }
    input:checked + label span:nth-child(1) {
    transform: rotate(45deg) translateY(14px);
    background-color: var(--main-special);
    }
    input:checked + label span:nth-child(2) {
    opacity: 0;
    transform: scale(0);
    }
    input:checked + label span:nth-child(3) {
    transform: rotate(-45deg) translateY(-14px);
    background-color: var(--main-special);
    }
</style>