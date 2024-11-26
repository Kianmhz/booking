export const useLocalAuth = defineStore('localAuth', () => {
	const {data} = useAuth()

	const hasPermission = (userPerm) => {
		if (data.value.permissions == 'all') {
			return true
		}

		if (typeof userPerm === 'string') {
			if (data.value.permissions.includes(userPerm)) {
				return true
			  }else {
				  return false
			  }
		}

		if (Array.isArray(userPerm)) {
			return userPerm.every(p => data.value.permissions.includes(p))
		}

		return false
	}

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

	const changeEmail = async (newEmail) => {
		const {data,error} = await useAPI('/userarea/change-email', {
			method:'POST',
			body: {
				email: newEmail
			}
		})

		if (data.value) {
			return data.value
		}
		if (error.value) {
			return false
		}
	}

	const changeUsername = async (newUsername) => {
		const {data,error} = await useAPI('/userarea/change-username', {
			method:'POST',
			body: {
				username: newUsername
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

	return { hasPermission, changePassword, changeEmail, changeUsername, changePersonalDetails }
})

if (import.meta.hot) {
	import.meta.hot.accept(acceptHMRUpdate(useLocalAuth, import.meta.hot))
}
