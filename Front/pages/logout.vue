<script setup>
useHead({
	title: 'Logout',
})

const { signOut } = useAuth()
signOut({ callbackUrl: '/auth' })

</script>

<template>
	<UCard>
		<div class="flex flex-col text-center gap-1 animate-pulse">
			<div class="text-2xl">Logging Out</div>
			<div>Loading ...</div>
		</div>
	</UCard>
</template>