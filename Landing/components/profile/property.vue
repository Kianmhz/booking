<template>
  <form @submit.prevent>
    <!-- Property Name and Location -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="propertyName" class="block text-sm font-medium text-gray-700">Property Name</label>
        <UInput
          class="mt-1"
          id="propertyName"
          v-model="property.name"
          placeholder="Enter property name"
          icon="material-symbols:store"
        />
      </div>
      <div class="form-group">
        <label for="propertyLocation" class="block text-sm font-medium text-gray-700">City/Country</label>
        <UInput
          class="mt-1"
          id="propertyLocation"
          v-model="property.location"
          placeholder="Enter city/country"
          icon="material-symbols:location-city"
        />
      </div>
    </div>
    <!-- Property Address -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="propertyAddress" class="block text-sm font-medium text-gray-700">Property Address</label>
        <UInput
          class="mt-1"
          id="propertyAddress"
          v-model="property.address"
          placeholder="Enter property address"
          icon="material-symbols:location-on"
        />
      </div>
    </div>
    <!-- Property Email and Phone -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="propertyEmail" class="block text-sm font-medium text-gray-700">Property Email</label>
        <UInput
          class="mt-1"
          id="propertyEmail"
          v-model="property.email"
          type="email"
          placeholder="Enter property email"
          icon="material-symbols:alternate-email"
        />
      </div>
      <div class="form-group">
        <label for="propertyPhone" class="block text-sm font-medium text-gray-700">Property Phone</label>
        <UInput
          class="mt-1"
          id="propertyPhone"
          v-model="property.phone"
          placeholder="Enter property phone"
          icon="ic:round-local-phone"
        />
      </div>
    </div>
    <!-- Property Cover Image -->
    <div class="mb-6">
      <label for="coverImage" class="block text-sm font-medium text-gray-700">Cover Image</label>
      <UInput
        id="coverImage"
        type="file"
        accept="image/*"
        @change="onFileChange"
        class="mt-1 block w-full"
      />
      <div v-if="filePreview" class="mt-4">
        <img :src="filePreview" alt="File Preview" class="w-full h-48 object-cover rounded-md" />
      </div>
    </div>
    <!-- About Property -->
    <div class="form-group mb-6">
      <label for="aboutProperty" class="block text-sm font-medium text-gray-700">About Property</label>
      <UTextarea
      class="mt-1"
        id="aboutProperty"
        v-model="property.description"
        placeholder="Enter details about the property"
      />
    </div>
    <!-- Action Buttons -->
    <div class="mt-6 text-right">
      <button
        v-if="!property.timestamp"
        @click="addProperty()"
        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
      >
        Add Property
      </button>
      <button
        v-if="property.timestamp"
        @click="editProperty()"
        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
      >
        Save Changes
      </button>
    </div>
  </form>
</template>

<script setup>
const config = useRuntimeConfig();
const apiHost = config.public.apiHost;
let property;

try {
  const result = await useFetch(`${apiHost}/monitor/property`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  property = ref(result.data.value.message);
} catch (error) {
  property = ref({});
  console.error('Error fetching property details:', error);
}

const onFileChange = (event, type) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = () => {
    if (type === 'coverImage') {
      property.value.image = reader.result;
    }
  };
  if (file) {
    reader.readAsDataURL(file);
  }
};

const editProperty = async () => {
  try {
    const result = await useFetch(`${apiHost}/property/edit`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(property.value),
    });

    property.value = result.data.value.message;
  } catch (error) {
    console.error('Error saving changes:', error);
  }
};

const addProperty = async () => {
  try {
    const result = await useFetch(`${apiHost}/property/new`, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(property.value),
    });

    property.value = result.data.value.message;
  } catch (error) {
    console.error('Error adding property:', error);
  }
};
</script>