<template>
  <div class="w-80 md:w-1/2 p-5 max-sm:pt-40">
    <form class="login">
      <h2 class="text-2xl text-center mb-10 text-[#8067e8] font-bold">Welcome Back!</h2>
      <BaseInput
        icon="material-symbols:account-circle-full"
        type="email"
        placeholder="Email"
        v-model="email"
        iconColor="text-[#8067e8]"
        borderColor="border-[#8067e8]"
        focusBorderColor="focus:border-[#8067e8]"
        textColor="text-gray-900"
      />
      <BaseInput
        icon="teenyicons:password-outline"
        type="password"
        placeholder="Password"
        v-model="password"
        iconColor="text-[#8067e8]"
        borderColor="border-[#8067e8]"
        focusBorderColor="focus:border-[#8067e8]"
        textColor="text-gray-900"
      />
      <div class="flex justify-between mt-10">
        <button @click="submitForm()" type="button" class="w-full py-3 px-5 bg-[#8067e8] text-white font-bold rounded-lg shadow-lg hover:bg-[#6b54d4] transition transform hover:scale-105">
          <span class="flex items-center justify-center">
            Log In
          </span>
        </button>
      </div>
    </form>
    <div class="flex items-center justify-center w-full my-5">
      <div class="h-px bg-gray-300 flex-grow"></div>
      <span class="mx-4 text-gray-600">or</span>
      <div class="h-px bg-gray-300 flex-grow"></div>
    </div>
    <div class="flex flex-col items-center mt-5">
      <nuxt-link to="/" class="flex items-center bg-white py-3 px-3 rounded-full border text-gray-700">
        <Icon name="ion:home" />
      </nuxt-link>
      <p class="mt-3 text-gray-600 mb-1">
        Don't have an account?
      </p>
      <a @click="$emit('switch-to-signup')" class="text-[#8067e8] font-bold cursor-pointer">Sign Up</a>
    </div>
  </div>
</template>

<script setup>
const toast = useToast();
const { signIn } = useAuth();

const email = ref('');
const password = ref('');

const submitForm = async () => {
  if (!email.value || !password.value) {
    toast.add({
      title: 'Please fill in all fields.',
      icon: 'i-heroicons-x-circle',
      color: 'red',
    });
    return;
  }

  const data = {
    email: email.value,
    password: password.value,
  };

  try {
    await signIn(data, { callbackUrl: '/profile' });
  } catch (err) {
    toast.add({
      title: 'Login failed. Please try again.',
      icon: 'i-heroicons-x-circle',
      color: 'red',
    });
  }
};
</script>
