<template>
    <div class="w-full mt-16 mb-10">
        <div class="banner rounded-b-[5%] text-white text-center py-36 w-full">
              <h1 class="text-4xl md:text-6xl font-bold">Help Center</h1>
              <p class="mt-4 text-lg md:text-2xl">How can we help you today?</p>
        </div>
        <UContainer>
            <div class="grid mt-8 mb-8 gap-8 grid-flow-row md:-mt-16 md:grid-flow-col md:grid-cols-3">
                <div @click="toggleFAQ" class="bg-[--sec-bg] shadow rounded-3xl p-16 flex flex-col items-center cursor-pointer hover:scale-105 transition">
                    <Icon name="line-md:question-circle" size="60" class="text-[--main-special] mb-4 text-5xl" />
                    <p class="text-lg font-semibold">FAQ</p>
                </div>
                <div @click="toggleContactUs" class="bg-[--sec-bg] shadow rounded-3xl p-16 flex flex-col items-center cursor-pointer hover:scale-105 transition">
                    <Icon name="line-md:account" size="60" class="text-[--main-special] mb-4 text-5xl" />
                    <p class="text-lg font-semibold">Contact Support</p>
                </div>
                <div @click="loadLiveChatScript" class="bg-[--sec-bg] shadow rounded-3xl p-16 flex flex-col items-center cursor-pointer hover:scale-105 transition">
                    <Icon name="line-md:chat" size="60" class="text-[--main-special] mb-4 text-5xl" />
                    <p class="text-lg font-semibold">Live Chat</p>
                </div>
            </div>
            <div class="bg-[--sec-bg] p-10 rounded-3xl shadow gap-y-8 grid grid-flow-row grid-cols-1 md:grid-flow-col md:grid-cols-2">
                <div>
                    <div v-show="Tabs.FAQ">
                        <HelpCenterFAQ />
                    </div>
                    <div v-show="Tabs.contactUs">
                        <HelpCenterContact />
                    </div>
                </div>
                <div class="flex justify-center items-center">
                  <nuxt-img src="https://via.placeholder.com/600" alt="FAQ Image" class="rounded-3xl shadow-lg w-80 h-80" />
                </div>
            </div>
        </UContainer>
    </div>
</template>

<script setup>
const activateLiveChat = ref(false);

const Tabs = reactive({
    FAQ: true,
    contactUs: false
});

const toggleFAQ = () => {
    Tabs.FAQ = true;
    Tabs.contactUs = false;
}

const toggleContactUs = () => {
    Tabs.FAQ = false;
    Tabs.contactUs = true;
}

const loadLiveChatScript = () => {
    activateLiveChat.value = !activateLiveChat.value;
    // Check if the script is already inserted to prevent multiple insertions
    if (!document.getElementById('tidio-chat-script')) {
        const script = document.createElement('script');
        script.src = "//code.tidio.co/j1ncln6k9tbjxcb5zr3iyr6nj2alcxjx.js";
        script.async = true;
        script.id = 'tidio-chat-script'; // Optional: Add an ID to easily find the script later
        document.head.appendChild(script);
    }

    if (activateLiveChat.value) {
        tidioChatApi.show();
        tidioChatApi.open();
    } else {
        tidioChatApi.hide();
    }
};
</script>
