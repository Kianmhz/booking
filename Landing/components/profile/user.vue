<script setup>
const config = useRuntimeConfig();
const apiHost = config.public.apiHost;
let formData = new FormData();
let user = useCookie("user");

// Submits the form
const saveChanges = async () => {
  try {
    const result = await useFetch(`${apiHost}/users/edit`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(user.value)
    });
    const resultUpload = await useFetch(`${apiHost}/uploads/${user.value.uuid}`, {
      method: 'POST',
      credentials: 'include',
      body: formData
    });
    console.log('Changes saved', result);
  } catch (error) {
    console.error('Error saving changes', error);
  }
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
  <form @submit.prevent="saveChanges">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="form-group">
        <label for="firstName" class="block text-sm font-medium text-[--light-text]">First Name</label>
        <BaseInput
          id="firstName"
          v-model="user.first_name"
          placeholder="Enter first name"
          icon="material-symbols:account-circle"
        />
      </div>
      <div class="form-group">
        <label for="lastName" class="block text-sm font-medium text-[--light-text]">Last Name</label>
        <BaseInput
          id="lastName"
          v-model="user.last_name"
          placeholder="Enter last name"
          icon="ph:signature-bold"
        />
      </div>
      <div class="form-group">
        <label for="mobileNumber" class="block text-sm font-medium text-[--light-text]">Mobile Number</label>
        <BaseInput
          id="mobileNumber"
          v-model="user.phone"
          placeholder="Enter mobile number"
          icon="majesticons:iphone-x-apps-line"
        />
      </div>
      <div class="form-group">
        <label for="emailId" class="block text-sm font-medium text-[--light-text]">Email ID</label>
        <BaseInput
          id="emailId"
          v-model="user.email"
          type="email"
          placeholder="Enter email ID"
          icon="material-symbols:alternate-email"
        />
      </div>
      <div class="form-group">
        <label for="dateOfBirth" class="block text-sm font-medium text-[--light-text]">Date of Birth</label>
        <BaseInput
          id="dateOfBirth"
          v-model="user.date_of_birth"
          type="date"
          placeholder="Enter date of birth"
          icon="material-symbols:cake"
        />
      </div>
    </div>
    <div class="mt-6 text-right">
      <button
        type="submit"
        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
      >
        Save Changes
      </button>
    </div>
  </form>
</template>
