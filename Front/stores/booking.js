export const useBooking = defineStore('booking', () => {

	const getBooking = async (page = 1, limit) => {
		const {data} = await useAPI('/rental/booking',{query:{_page:page, _limit:limit}})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const addBooking = async (booking_data) => {
		const {data} = await useAPI('/rental/booking/',{method:'POST', body: booking_data})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const editBooking = async (id, booking_data) => {
		const {data} = await useAPI(`/rental/booking/${id}/`,{method:'PUT', body: booking_data})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const deleteBooking = async (id) => {
		const {data} = await useAPI(`/rental/booking/${id}/`,{method:'DELETE'})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}



	return {
		getBooking,
		addBooking,
		editBooking,
		deleteBooking,
	}

})


if (import.meta.hot) {
	import.meta.hot.accept(acceptHMRUpdate(useBooking, import.meta.hot))
}
