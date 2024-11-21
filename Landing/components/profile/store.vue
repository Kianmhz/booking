<template>
  <form @submit.prevent>
    <!-- Store Name and Location -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="storeName" class="block text-sm font-medium text-gray-700">Store Name</label>
        <BaseInput
          id="storeName"
          v-model="store.name"
          placeholder="Enter store name"
          icon="material-symbols:store"
        />
      </div>
      <div class="form-group">
        <label for="storeLocation" class="block text-sm font-medium text-gray-700">City/Country</label>
        <BaseInput
          id="storeLocation"
          v-model="store.country"
          placeholder="Enter city/country"
          icon="material-symbols:location-city"
        />
      </div>
    </div>
    <!-- Store Address and Location Description -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="storeAddress" class="block text-sm font-medium text-gray-700">Store Address</label>
        <BaseInput
          id="storeAddress"
          v-model="store.address"
          placeholder="Enter store address"
          icon="material-symbols:location-on"
        />
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="storeEmail" class="block text-sm font-medium text-gray-700">Store Email</label>
        <BaseInput
          id="storeEmail"
          v-model="store.email"
          type="email"
          placeholder="Enter store email"
          icon="material-symbols:alternate-email"
        />
      </div>
      <div class="form-group">
        <label for="storePhone" class="block text-sm font-medium text-gray-700">Store Phone</label>
        <BaseInput
          id="storePhone"
          v-model="store.phone"
          placeholder="Enter store phone"
          icon="ic:round-local-phone"
        />
      </div>
    </div>
    <!-- Store Cover Image -->
    <div class="form-group mb-6">
      <label for="coverImage" class="block text-sm font-medium text-gray-700">Cover Image</label>
      <input
        type="file"
        id="coverImage"
        @change="onFileChange($event, 'coverImage')"
        class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
      />
      <div v-if="store.image" class="mt-4">
        <img :src="store.image" alt="Cover Image Preview" class="w-full h-48 object-cover rounded-md">
      </div>
    </div>
    <!-- About Store -->
    <div class="form-group mb-6">
      <label for="aboutStore" class="block text-sm font-medium text-gray-700">About Store</label>
      <textarea
        id="aboutStore"
        v-model="store.description"
        class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
      ></textarea>
    </div>
    <div class="mt-6 text-right">
      <button
        v-if="!store.timestamp"
        @click="addStore()"
        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
      >
        Add Store
      </button>
      <button
        v-if="store.timestamp"
        @click="editStore()"
        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
      >
        Save changes
      </button>
    </div>
  </form>
</template>

<script setup>
const config = useRuntimeConfig()
const apiHost = config.public.apiHost
let store;

try {
  const result = await useFetch(`${apiHost}/monitor/store`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json'
    },
  });

  store = ref(result.data.value.message);
} catch (error) {
  store = ref({});
  console.error('Error saving changes', error)
}

const onFileChange = (event, type) => {
  const file = event.target.files[0]
  const reader = new FileReader()
  reader.onload = () => {
    if (type === 'coverImage') {
      store.value.image = reader.result
    }
  }
  if (file) {
    reader.readAsDataURL(file)
  }
}

const editStore = async () => {
  try {
    const result = await useFetch(`${apiHost}/store/edit`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(store.value)
    });

    store.value = result.data.value.message;
  } catch (error) {
    console.error('Error saving changes', error)
  }
}

const addStore = async () => {
  try {
    const result = await useFetch(`${apiHost}/store/new`, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(store.value)
    });

    store.value = result.data.value.message;
  } catch (error) {
    console.error('Error saving changes', error)
  }
}
</script>
