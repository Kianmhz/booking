<script setup>
useHead({
	titleTemplate: (titleChunk) => {
		return titleChunk ? `${titleChunk} - Milestone` : 'Milestone';
	}
})


const {refresh,token} = useAuth();
try {
    if (!token.value) {
      const x = await refresh();
      if (x) {
        navigateTo("/profile");
      }
    }
}catch(e) {
    console.log(e);
}


</script>


<template>
  <div>
    <NuxtLoadingIndicator/>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
    <UNotifications/>
  </div>
</template>