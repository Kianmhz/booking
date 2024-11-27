<script setup>
// const toast = useToast()
const isModalOpen = ref(false)
const toast = useToast()
const localAuthStore = useLocalAuth()

defineExpose ({
	isModalOpen
})

const loading = ref(false)

const state = reactive({
	oldPassword: '',
	newPassword: '',
	confirmPassword: '',
})

const validate = (state) => {
	const errors = []
	if (!state.oldPassword) errors.push({ path: 'oldPassword', message: 'Required' })
	if (!state.newPassword) errors.push({ path: 'newPassword', message: 'Required' })
	if (!state.confirmPassword) errors.push({ path: 'confirmPassword', message: 'Required' })
	if (state.newPassword !== state.confirmPassword) errors.push({ path: 'confirmPassword', message: 'Passwords do not match' })
	return errors
}

const changePassword = async () => {
	loading.value = true
	const res = await localAuthStore.changePassword(state.oldPassword, state.newPassword)
	loading.value = false
	if (res) {
		toast.add({
			title: 'Password changed successfully',
			icon: 'i-heroicons-check-badge',
			color: 'green'
		})
		isModalOpen.value = false
	}else {
		toast.add({
			title: 'Failed to change password',
			icon: 'i-heroicons-x-circle',
			color: 'red'
		})
	}
}

watch(isModalOpen, async (value) => {
	if (value) {
		state.oldPassword = ''
		state.newPassword = ''
		state.confirmPassword = ''
	}
})

</script>


<template>
	<UModal v-model="isModalOpen">
		<UCard>
			<template #header>
				Change Password
			</template>
			<UForm class="flex flex-col gap-2" :state="state" :validate="validate" @submit="changePassword">
				<UFormGroup label="Current Password" name="oldPassword">
					<UInput v-model="state.oldPassword" type="password"/>
				</UFormGroup>
				<UDivider class="my-1"/>
				<UFormGroup label="New Password" name="newPassword">
					<UInput v-model="state.newPassword" type="password"/>
				</UFormGroup>
				<UFormGroup label="Confirm Password" name="confirmPassword">
					<UInput v-model="state.confirmPassword" type="password"/>
				</UFormGroup>
				<UButton type="submit" :loading="loading" block>Confirm</UButton>
			</UForm>

		</UCard>

	</UModal>
</template>