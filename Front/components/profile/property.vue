<template>
  <form @submit.prevent>
    <!-- Property Name and Location -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div class="form-group">
        <label for="propertyName" class="block text-sm font-medium text-gray-700">Property Name</label>
        <UInput
          class="mt-1"
          id="propertyName"
          v-model="property.title"
          placeholder="Enter property name"
          icon="material-symbols:store"
        />
      </div>
      <div class="form-group">
        <label for="propertyAddress" class="block text-sm font-medium text-gray-700">Property Address</label>
        <UInput
          class="mt-1"
          id="propertyAddress"
          v-model="property.location"
          placeholder="Enter property address"
          icon="material-symbols:location-on"
        />
      </div>
      <div class="form-group">
        <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
        <UInput
          class="mt-1"
          id="price"
          v-model="property.price"
          placeholder="Enter price"
          icon="material-symbols:location-on"
        />
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

    <!-- <UploadDrop ref="dropzone"/>

    <UCard>
      <div class="grid lg:grid-cols-3 gap-5">
        <UCard v-for="myFile in mediaUIList">
          <template #header>
            <div class="flex justify-between items-center">
              <div class="text-sm">
              </div>
              <div>
                <UBadge size="sm" color="blue" variant="outline">
                  <div v-if="getFileType(myFile.link) == 'image'">Image</div>
                  <div v-else-if="getFileType(myFile.link) == 'video'">Video</div>
                  <div v-else>Unknown extension</div>
                </UBadge>
              </div>
            </div>
          </template>
          <div v-if="myFile.status == 2">
            <img v-if="getFileType(myFile.link) == 'image'" :src="myFile.link" class="h-40 mx-auto object-contain mb-4 rounded" alt="">
          </div>
          <template #footer>
            <div class="result">
              <div v-if="myFile.status == 1">
                <UProgress :value="myFile.progress"/>
                <span>{{ myFile.progress }}%</span>
              </div>
              <div v-else-if="myFile.status == 2">
                <UButton color="primary" size="xs" icon="i-heroicons-link" @click="copyToClipboard(myFile.link)">Copy link</UButton>
                <UButton color="red" size="xs" icon="i-heroicons-trash" @click="removeMedia(myFile.id)"/>
              </div>
              <div v-else-if="myFile.status == 3">
                <span class="text-red-600">Failed to upload</span>
              </div>
            </div>
          </template>
        </UCard>
      </div>
      </UCard> -->
      <div class="mt-6 text-right">
        <UButton
          @click="sendProperty()"
          type="submit"
        >
          Save Changes
        </UButton>
      </div>
  </form>
</template>

<script setup>
const toast = useToast();

const exploreStore = useExplore()

const dropzone = ref(null)
const property = reactive({
  title: '',
  location: '',
  price: '',
  description: '',
})

const sendProperty = async () => {
  const res = await exploreStore.addExplore({...property})
  if (res) {
    toast.add({
      title: 'Property added successfully',
      icon:"i-heroicons-check-badge"
    });
    property.title = ''
    property.location = ''
    property.price = ''
    property.description = ''
  }else {
    toast.add({
      title: 'Failed to add property',
      icon:"i-heroicons-x-circle",
			color: 'red'
    });
  }
}

// const allNotUploadedFiles = computed(() => {
//  return dropzone.value?.allNotUploadedFiles
// })

// const dropUploadedFiles = computed(() => {
//  return dropzone.value?.allUploadedFiles
// })

// const mediaUIList = computed(() => {
//  // const x = product.media.map((media) => {
//  //  // product.site_gallery is array of object with id
//  //  const site_view = product.site_gallery.some((site) => site.id === media.id);
//  //  const reseller_view = product.gallery.some((reseller) => reseller.id === media.id);
//  //  return {
//  //   ...media,
//  //   status:2,
//  //   site_view,
//  //   reseller_view,
//  //  }
//  // })
//   const x = []
//  if (!allNotUploadedFiles.value) return x;
//  const y = allNotUploadedFiles.value

//  return [...x, ...y]
// })
</script>