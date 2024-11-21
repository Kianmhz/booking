
<template>
  <nav class="bg-[--sec-bg] pb-4">
    <UContainer>
      <div class="flex justify-center">
        <a v-for="page in [1, 2]" href="#" class="border-transparent text-[--text] hover:text-[--sec-special] hover:border-[--sec-special] border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> {{page}} </a>
        <a href="#" class="border-[--main-special] text-[--main-special] border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium" aria-current="page"> 3 </a>
        <span class="border-transparent text-[--text]border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> ... </span>
        <a v-for="page in [8, 9]" href="#" class="border-transparent text-[--text] hover:text-[--sec-special] hover:border-[--sec-special] border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> {{page}} </a>
      </div>
    </UContainer>
  </nav>
</template>