export const copyToClipboard = async (text) => {
    const toast = useToast()
	try {
		await navigator.clipboard.writeText(text)
		toast.add({
			title: 'Copied to clipboard',
			icon:"i-heroicons-check-badge"
		})
	} catch (err) {
		toast.add({
			title: 'Failed to copy to clipboard',
			icon:"i-heroicons-x-circle",
			color: 'red'
		})
	}
}