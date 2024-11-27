<script setup>
const { data: user } = useAuth(); // Fetch user data from useAuth
const authStore = useLocalAuth(); // Pinia store
const toast = useToast();

const passwordModal = ref(null);

const userDetails = reactive({
  fullname: '',
  email: '',
});

// Initialize user details
if (user.value) {
  userDetails.fullname = user.value.fullname || '';
  userDetails.email = user.value.email || '';
}

const openPasswordModal = () => {
  passwordModal.value.isModalOpen = true;
};

const saveChanges = async () => {
  try {
    if (!userDetails.fullname || !userDetails.email) {
      toast.add({
        title: 'Error',
        description: 'Please fill in all required fields.',
        icon: 'i-heroicons-x-circle',
        color: 'red',
      });
      return;
    }

    const updatedDetails = {
      fullname: userDetails.fullname,
      email: userDetails.email,
    };

    const result = await authStore.changePersonalDetails(user.value.id, updatedDetails);

    if (result) {
      toast.add({
        title: 'Success',
        description: 'Profile updated successfully!',
        icon: 'i-heroicons-check-circle',
        color: 'green',
      });
    } else {
      toast.add({
        title: 'Error',
        description: 'Failed to update profile. Please try again.',
        icon: 'i-heroicons-x-circle',
        color: 'red',
      });
    }
  } catch (error) {
    toast.add({
      title: 'Error',
      description: 'An unexpected error occurred. Please try again.',
      icon: 'i-heroicons-x-circle',
      color: 'red',
    });
  }
};
</script>

<template>
  <form @submit.prevent="saveChanges">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="form-group">
        <label for="fullname" class="block text-sm font-medium text-gray-700">Full Name</label>
        <UInput
          class="mt-1"
          id="fullname"
          v-model="userDetails.fullname"
          placeholder="Enter Full name"
          icon="material-symbols:account-circle"
        />
      </div>
      <div class="form-group">
        <label for="emailId" class="block text-sm font-medium text-gray-700">Email ID</label>
        <UInput
          class="mt-1"
          id="emailId"
          v-model="userDetails.email"
          type="email"
          placeholder="Enter email ID"
          icon="material-symbols:alternate-email"
        />
      </div>

      <UCard>
        <UFormGroup label="Password">
          <UButton icon="i-ph-fingerprint" @click="openPasswordModal()">Change Password</UButton>
        </UFormGroup>
      </UCard>
    </div>
    <div class="mt-6 text-right">
      <UButton type="submit">
        Save Changes
      </UButton>
    </div>
  </form>
  <LazyModalChangePassword ref="passwordModal" />
</template>
