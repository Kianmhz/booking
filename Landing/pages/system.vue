<script setup>
const config = useRuntimeConfig();
const apiHost = config.public.apiHost + '/';
const responseTimes = ref([]);
const averageResponseTime = ref(0);
const averageSuccessRate = ref(0);
const operationalThreshold = 0.6; // Set your threshold here

onMounted(() => {
  setInterval(async () => {
    const start = performance.now();

    await $fetch(apiHost).then((res) => {
      if (res.status === 0) {
        averageSuccessRate.value += 1;
      }
    }).catch(() => {
      averageSuccessRate.value -= 1;
    });

    const end = performance.now();
    responseTimes.value.push(end - start);

    if (responseTimes.value.length > 0) {
      averageResponseTime.value = parseFloat((responseTimes.value.reduce((a, b) => a + b, 0) / responseTimes.value.length).toFixed(2));
    }
  }, 1000);
});

const successRate = computed(() => {
  return responseTimes.value.length > 0 ? parseFloat(((averageSuccessRate.value / responseTimes.value.length) * 100).toFixed(2)) : 0;
});

const isOperational = computed(() => {
  return successRate.value >= operationalThreshold * 100;
});
</script>

<template>
  <UContainer>
    <div class="flex items-center justify-center pt-16 my-10">
      <div class="max-w-4xl w-full bg-[--sec-bg] p-10 rounded-3xl shadow">
        <!-- Status Indicator -->
        <div class="text-center mb-8">
          <div class="relative mb-6 flex items-center justify-center">
            <div class="absolute inset-0 flex items-center justify-center">
              <Icon 
                :name="isOperational ? 'material-symbols:check-small-rounded' : 'material-symbols:close-rounded'"
                size="60"
                :class="isOperational ? 'text-green-500' : 'text-red-500'"
              />
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44" class="w-24 h-24">
              <g fill="none" fill-rule="evenodd" stroke-width="2" :stroke="isOperational ? '#34D399' : '#EF4444'">
                <circle cx="22" cy="22" r="1">
                  <animate attributeName="r" begin="0s" calcMode="spline" dur="1.8s" keySplines="0.165, 0.84, 0.44, 1" keyTimes="0; 1" repeatCount="indefinite" values="1; 20" />
                  <animate attributeName="stroke-opacity" begin="0s" calcMode="spline" dur="1.8s" keySplines="0.3, 0.61, 0.355, 1" keyTimes="0; 1" repeatCount="indefinite" values="1; 0" />
                </circle>
                <circle cx="22" cy="22" r="1">
                  <animate attributeName="r" begin="-0.9s" calcMode="spline" dur="1.8s" keySplines="0.165, 0.84, 0.44, 1" keyTimes="0; 1" repeatCount="indefinite" values="1; 20" />
                  <animate attributeName="stroke-opacity" begin="-0.9s" calcMode="spline" dur="1.8s" keySplines="0.3, 0.61, 0.355, 1" keyTimes="0; 1" repeatCount="indefinite" values="1; 0" />
                </circle>
              </g>
            </svg>
          </div>
          <h1 class="text-3xl font-bold">{{ isOperational ? 'All systems operational' : 'Systems not operational' }}</h1>
          <p class="mt-3 text-[--light-text]">All Engines</p>
        </div>
  
        <!-- Success Rate -->
        <div class="mb-10">
          <div class="flex justify-between items-center">
            <h2 class="text-xl font-semibold">Success rate</h2>
            <span :class="isOperational ? 'text-green-500' : 'text-red-500'">{{ isOperational ? 'Operational' : 'Not operational' }}</span>
          </div>
          <div class="my-3">
            <UMeter color="green" :value="successRate" />
          </div>
          <div class="text-right text-[--light-text] text-sm">{{ successRate }}%</div>
        </div>
  
        <!-- Response Time -->
        <div class="mb-10">
          <div class="flex justify-between items-center">
            <h2 class="text-xl font-semibold">Response time</h2>
          </div>
          <div class="my-3">
            <UMeter color="blue" :value="100-averageResponseTime" />
          </div>
          <div class="text-right text-[--light-text] text-sm">{{ averageResponseTime }}ms</div>
        </div>
  
        <!-- Recent Notices -->
        <div>
          <h2 class="text-xl font-semibold mb-4">Recent notices</h2>
          <div class="bg-[--main-bg] p-5 rounded-lg mb-4">
            <div class="flex justify-between items-center mb-2">
              <p class="text-sm">Error message here issues with syncing problem and can't read the description</p>
              <span class="text-green-500">Resolved</span>
            </div>
            <div class="text-sm text-[--light-text]">
              <p>Started: April 16, 2023 - 11:12:24</p>
              <p>Closed: April 16, 2023 - 19:12:24</p>
              <p>Status: Resolved after 8 hours</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </UContainer>
</template>
