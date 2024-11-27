export const useLocalAuth = defineStore('localAuth', () => {

	const changePassword = async (current_password,newPassword) => {
		const {data,error} = await useAPI('/userarea/change-pass', {
			method:'POST',
			body: {
				current_password: current_password,
				new_password: newPassword
			}
		})

		if (data.value) {
			return data.value
		}
		if (error.value) {
			return false
		}
	}

	const changePersonalDetails = async (user_id,details) => {
		const {data,error} = await useAPI(`/userarea/user-profile/${user_id}/`, {
			method:'PUT',
			body: details
		})

		if (data.value) {
			return data.value
		}
		if (error.value) {
			return false
		}
	}

	return { changePassword, changePersonalDetails }
})

if (import.meta.hot) {
	import.meta.hot.accept(acceptHMRUpdate(useLocalAuth, import.meta.hot))
}
