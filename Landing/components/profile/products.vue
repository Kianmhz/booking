<template>
    <div class="products-editor">
      <h3 class="text-xl font-semibold text-gray-800 mb-4">Products</h3>
      <div v-for="(product, index) in products" :key="index" class="border p-4 rounded mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-4">
          <div class="form-group">
            <label :for="`productName${index}`" class="block text-sm font-medium text-gray-700">Product Name</label>
            <input :id="`productName${index}`" v-model="product.name" class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          </div>
          <div class="form-group">
            <label :for="`productPrice${index}`" class="block text-sm font-medium text-gray-700">Product Price</label>
            <input :id="`productPrice${index}`" v-model="product.price" type="number" class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-4">
          <div class="form-group">
            <label :for="`productName${index}`" class="block text-sm font-medium text-gray-700">Status</label>
            <select :id="`productName${index}`" v-model="product.status" class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="Available">Available</option>
              <option value="Ordered">Ordered</option>
              <option value="Unavailable">Unavailable</option>
              <option value="OutOfStock">Out of Stock</option>
            </select>
          </div>
          <div class="form-group">
            <label :for="`productQuantity${index}`" class="block text-sm font-medium text-gray-700">Quantity</label>
            <input  :id="`productQuantity${index}`" v-model="product.quantity" type="number" class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          </div>
        </div>
        <div class="form-group">
          <label :for="`productImage${index}`" class="block text-sm font-medium text-gray-700">Product Image</label>
          <input :id="`productImage${index}`" type="file" @change="onFileChange($event, index)" class="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          <div v-if="product.imagePreview" class="mt-4">
            <img :src="product.imagePreview" alt="Product Image Preview" class="w-full h-40 object-cover rounded-md">
          </div>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-2 gap-6 mb-4">
          <button type="button" @click="removeProduct(index)" class="mt-4 text-red-500 hover:text-red-700">Remove Product</button>
          <button v-if="product.item_id" type="button" @click="editProduct(index)" class="mt-4 text-blue-500 hover:text-blue-700">Edit</button>
          <button v-if="!product.item_id" type="button" @click="submitProduct(index)" class="mt-4 text-green-500 hover:text-green-700">Submit</button>
        </div>
      </div>
      <button type="button" @click="addProduct" class="text-blue-500 hover:text-blue-700">Add Product</button>
    </div>
</template>
  
<script setup>
const config = useRuntimeConfig()
const apiHost = config.public.apiHost
let formData = new FormData();
const products = ref([]);

const result = await useAPI('GET', '/monitor/inventory', {
  server: false,
  lazy: true,
})
products = result.data.value.message.items;

try {
  const result = await useFetch(`${apiHost}/monitor/inventory`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json'
    },
  });

  products = ref(result.data.value.message.items);
} catch (error) {
  console.error('Error saving changes', error)
}

const emit = defineEmits(['update:products'])
watch(products, (newProducts) => {
emit('update:products', newProducts)
}, { deep: true })

const onFileChange = (event, index) => {
const file = event.target.files[0]
const reader = new FileReader()
reader.onload = () => {
    formData.set('file', file);
    products.value[index].imagePreview = reader.result
}
if (file) {
    reader.readAsDataURL(file)
}
}

const addProduct = () => {
  products.value.push({ status: 'Available', name: '', company: '', price: 0, quantity: 0, image: '', description: ''})
}

const removeProduct = async (index) => {

  try {
    const result = await useFetch(`${apiHost}/inventory/item`, {
      method: 'DELETE',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(products.value[index].item_id)
    });
    products.value.splice(index, 1)
  } catch (error) {
    console.error('Error saving changes', error)
  }

}

const submitProduct = async (index) => {

try {
    const result = await useFetch(`${apiHost}/inventory/item`, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(products.value[index])
    });

    products.value[index] = result.data.value.message;

    const resultUpload = await useFetch(`${apiHost}/uploads/${products.value[index].item_id}`, {
      method: 'POST',
      credentials: 'include',
      body: formData
    });
  } catch (error) {
    console.error('Error saving changes', error)
  }

}

const editProduct = async (index) => {

  try {
    const result = await useFetch(`${apiHost}/inventory/item`, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(products.value[index])
    });

    const resultUpload = await useFetch(`${apiHost}/uploads/${products.value[index].item_id}`, {
      method: 'POST',
      credentials: 'include',
      body: formData
    });

    products.value[index] = result.data.value.message;
  } catch (error) {
    console.error('Error saving changes', error)
  }

}
</script>