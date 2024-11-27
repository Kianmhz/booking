<script setup>
// const uploaderStore = useUploader()
const fileList = reactive([])

const upload = (files) => {
	Array.from(files).forEach(file => {
		fileList.push({
			file: file,
			link: '', // Download Link as the Result
			offset: 0, // Offset : Total Bytes Uploaded
			id: null, // Required for Chunk Uploading
			status: 0, // 0 Pending, 1 Uploading, 2 Uploaded, 3 Error
			progress: 0, // Percentage Progress
			reseller_view: true,
			site_view: false,
		})
	})
}

watch(fileList, async (files) => {
	// Check if upload is not yet initiated
	const validFiles = files.filter(file => file.status === 0);
	await Promise.all(validFiles.map(uploadNextChunk));
})

const fileInput = ref(null)

const dropData = reactive({
	active: false,
	hover: false,
})

const setActive = () => {
	dropData.active = true;
};

const setInactive = (e) => {
  if (e && e.currentTarget && !e.currentTarget.contains(e.relatedTarget)) {
    dropData.active = false;
  }
};

const openFileDialog = () => {
	fileInput.value.click()
}

const addToFiles = (e) => {
	// Check if Items are Dropped or Selected using dialog
	const eventFileList = e.target.files || e.dataTransfer.files

	// Cancel the Drop Class
	dropData.active = false;

	// Add Files to the List
	// uploaderStore.upload(eventFileList)
	upload(eventFileList)
}

const getActiveClass = () => {
	if (dropData.active) {
		return 'active-drop';
	}
};

// const deleteFile = (id) => {
// 	fileList.splice(id, 1)
// }

const allUploadedFiles = computed(() => {
	return fileList.filter(file => file.status === 2)
})

const allNotUploadedFiles = computed(() => {
	return fileList.filter(file => file.status !== 2)
})

const resetFiles = () => {
	// remove all files in filelist
	fileList.splice(0, fileList.length)
}

defineExpose({
	allUploadedFiles,
	allNotUploadedFiles,
	resetFiles,
})


</script>

<template>
<div
:class="getActiveClass()" class="border-4 border-dashed w-full flex items-center justify-center h-80 border-gray-100 dark:border-gray-800 cursor-pointer" for="dropzone-file" @dragenter.prevent="setActive" @dragover.prevent="setActive" @dragleave.prevent="setInactive"
				@drop.prevent="addToFiles" @click="openFileDialog">
    <div class="flex flex-col items-center">
		<UIcon name="i-ph-cloud-arrow-up" class="text-6xl mb-2 rounded-full p-2" dynamic/>
        <p class="mb-2 text-sm"><span class="font-semibold">Drop the files here</span> or <span class="font-semibold text-primary">Click here</span></p>
        <p class="text-xs">Any extenstion is accepted</p>
        <p class="text-xs">Max file size 100MB</p>
    </div>
</div>
<input ref="fileInput" type="file" class="hidden" multiple="multiple" @change="addToFiles">
</template>

<style scoped>
.active-drop {
	@apply border-green-600 bg-primary-400/10
}
</style>