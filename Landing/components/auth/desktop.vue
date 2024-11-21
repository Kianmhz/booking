<template>
    <div class="grid grid-flow-col grid-cols-3 h-screen w-screen relative overflow-hidden">
        <div class="bg-white z-50 col-span-2">
            <div class="screen-content flex justify-center items-center h-full tranistion duration-1000" :class="{ hidden: isHidden }">
                <AuthLogin v-if="!isSignUp" @switch-to-signup="showSignUp" />
                <AuthSignup v-if="isSignUp" @switch-to-login="showLogin" />
            </div>
        </div>
        <div class="bg-[var(--screen-bg)] transition duration-1000">
            <span class="screen__background__shape shape4" :class="{ moved4: isHidden }"></span>
            <span class="screen__background__shape shape3" :class="{ moved3: isHidden }"></span>    
            <span class="screen__background__shape shape2" :class="{ moved2: isHidden }"></span>
        </div>    
    </div>
  </template>
  
  <script setup>
  const isHidden = ref(false);
  const isSignUp = ref(false);
  
  function hideFields() {
    isHidden.value = true;
  }
  
  function showSignUp() {
    hideFields();
    setTimeout(() => {
      isHidden.value = false;
      isSignUp.value = true;
    }, 1000); // Delay for shapes to move out
  }
  
  function showLogin() {
    hideFields();
    setTimeout(() => {
      isHidden.value = false;
      isSignUp.value = false;
    }, 1000); // Delay for shapes to move out
  }
  
  watch(isSignUp, (newVal) => {
    const root = document.documentElement;
    if (newVal) {
      root.style.setProperty('--screen-bg', '#4683f7'); // Changing to a solid blue for the screen background
      root.style.setProperty('--shape2-bg', 'linear-gradient(135deg, #4683f7, #3b6ed1)');
      root.style.setProperty('--shape3-bg', 'linear-gradient(135deg, #3b6ed1, #5c94fa)');
      root.style.setProperty('--shape4-bg', 'linear-gradient(135deg, #5c94fa, #7aaeff)');
    } else {
      root.style.setProperty('--screen-bg', '#8067e8'); // Changing to a solid purple for the screen background
      root.style.setProperty('--shape2-bg', 'linear-gradient(135deg, #8067e8, #6a51c5)');
      root.style.setProperty('--shape3-bg', 'linear-gradient(135deg, #6a51c5, #947bf5)');
      root.style.setProperty('--shape4-bg', 'linear-gradient(135deg, #947bf5, #b49fff)');
    }
  });
  
  onMounted(() => {
    const root = document.documentElement;
    root.style.setProperty('--screen-bg', '#8067e8'); // Changing to a solid purple for the screen background
      root.style.setProperty('--shape2-bg', 'linear-gradient(135deg, #8067e8, #6a51c5)');
      root.style.setProperty('--shape3-bg', 'linear-gradient(135deg, #6a51c5, #947bf5)');
      root.style.setProperty('--shape4-bg', 'linear-gradient(135deg, #947bf5, #b49fff)');
  });
  
  </script>
  
  <style scoped>
  :root {
    --screen-bg: #5D54A4;
    --shape2-bg: #6C63AC;
    --shape3-bg: #7C78B8;
    --shape4-bg: #7E7BB9;
  }
  
  .screen-content {
    animation: contentAnimation 1s ease-in-out;
  }

  .screen__background__shape {
    position: absolute;
    animation: shapeAnimation 5s infinite alternate;
    transition: all 1s ease-in-out;
  }
  
  .shape2 {
    @apply h-[230px] w-[230px] -top-[150px] right-[40px] rounded-[42px] transition-all duration-1000 ease-in-out;
    background: var(--shape2-bg);
  }
  
  .shape3 {
    @apply h-[740px] w-[330px] top-[20px] -right-[50px] rounded-[32px] transition-all duration-1000 ease-in-out;
    background: var(--shape3-bg);
  }
  
  .shape4 {
    @apply h-[400px] w-[400px] top-[780px] -right-[100px] rounded-[60px] transition-all duration-1000 ease-in-out;
    background: var(--shape4-bg);
  }
  
  .moved2 {
    @apply -top-[500px];
  }
  
  .moved3 {
    @apply -right-[800px];
  }
  
  .moved4 {
    @apply top-[1500px];
  }
  </style>