<template>
  <h1 class="text-3xl font-bold mb-4">Contact Support</h1>
  <p class="text-[--light-text] mb-8">If you need assistance, please fill out the form below and our support team will get back to you as soon as possible.</p>
  
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div class="relative">
      <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
      <div class="mt-1">
        <UInput
          id="name"
          v-model="form.name"
          placeholder="Enter your name"
          icon="material-symbols:account-circle"
        />
        <span v-if="errors.name" class="text-red-500 text-sm absolute right-2 top-9">{{ errors.name }}</span>
      </div>
    </div>

    <div class="relative">
      <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
      <div class="mt-1">
        <UInput
          id="email"
          v-model="form.email"
          type="email"
          placeholder="Enter your email"
          icon="material-symbols:alternate-email"
        />
        <span v-if="errors.email" class="text-red-500 text-sm absolute right-2 top-9">{{ errors.email }}</span>
      </div>
    </div>

    <div class="relative">
      <label for="message" class="block text-sm font-medium text-gray-700">Message</label>
      <div class="mt-1">
        <UTextarea
          v-model="form.message"
          id="message"
          rows="4"
          placeholder="Enter your message"
        ></UTextarea>
        <span v-if="errors.message" class="text-red-500 text-sm absolute right-2 top-9">{{ errors.message }}</span>
      </div>
    </div>

    <div class="flex justify-end">
      <button
        type="submit"
        class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        Submit
      </button>
    </div>
  </form>
</template>

<script setup>
const form = ref({
  name: '',
  email: '',
  message: ''
});

const errors = ref({
  name: '',
  email: '',
  message: ''
});

const validateForm = () => {
  let valid = true;
  errors.value = {
    name: '',
    email: '',
    message: ''
  };

  if (!form.value.name) {
    errors.value.name = 'Name is required.';
    valid = false;
  }

  if (!form.value.email) {
    errors.value.email = 'Email is required.';
    valid = false;
  } else if (!/\S+@\S+\.\S+/.test(form.value.email)) {
    errors.value.email = 'Email is invalid.';
    valid = false;
  }

  if (!form.value.message) {
    errors.value.message = 'Message is required.';
    valid = false;
  }

  return valid;
};

const handleSubmit = () => {
  if (validateForm()) {
    alert('Form submitted successfully!');
    // Handle form submission (e.g., send data to the server)
    form.value = {
      name: '',
      email: '',
      message: ''
    };
  }
};
</script>
