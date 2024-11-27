export const useExplore = defineStore('explore', () => {
	const exploreList = ref([])


	const getExplore = async (page = 1, limit) => {
		const {data} = await useAPI('/rental/properties',{query:{_page:page, _limit:limit}})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const getSingleExplore = async (id) => {
		const {data} = await useAPI(`/rental/properties/${id}`)
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const addExplore = async (explore_data) => {
		const {data} = await useAPI('/rental/properties/',{method:'POST', body: explore_data})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const editExplore = async (id, explore_data) => {
		const {data} = await useAPI(`/rental/properties/${id}/`,{method:'PUT', body: explore_data})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const deleteExplore = async (id) => {
		const {data} = await useAPI(`/rental/properties/${id}/`,{method:'DELETE'})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const getReviews = async (id) => {
		const {data} = await useAPI('/rental/review/',{query:{property_id:id}})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const sendReview = async (review_data) => {
		const {data} = await useAPI('/rental/review/',{method:'POST', body: review_data}) // review_property should be id of property
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	const deleteReview = async (id) => {
		const {data} = await useAPI(`/rental/review/${id}/`,{method:'DELETE'})
		if (data.value) {
			return data.value
		}else {
			return false
		}
	}

	return {
		getExplore,
		getSingleExplore,
		addExplore,
		editExplore,
		deleteExplore,
		exploreList,

		getReviews,
		sendReview,
		deleteReview,
	}

})


if (import.meta.hot) {
	import.meta.hot.accept(acceptHMRUpdate(useExplore, import.meta.hot))
}
