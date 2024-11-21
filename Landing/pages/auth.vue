<script setup>
definePageMeta({
  layout: 'auth',
  colorMode: 'light',
});

// Reactive form data
const formData = ref({
  name: '',
  email: '',
  password: ''
});

// Submits the form
const formSubmit = async (request) => {
  try {
    const result = request == "signin" ? await formSignin() : await formSignup();
    console.log(result);
  } catch (error) {
    console.error('Contact form could not be sent', error);
  }
};

// Makes an HTTP request to send the form data
const formSignin = async () => {
  return await $fetch(`${apiHost}/users/signin`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email: formData.value.email,
      password: formData.value.password,
      phone: "0000000000"
    }),
  });
};

const formSignup = async () => {
  return await useFetch(`${apiHost}/users/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      first_name: formData.value.name,
      email: formData.value.email,
      password: formData.value.password,
      phone: "0000000000"
    }),
  });
};

</script>

<template>
    <div class="sm:hidden">
      <AuthMobile />
    </div>
    <div class="max-sm:hidden">
      <AuthDesktop />
    </div>
</template>