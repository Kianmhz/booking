<template>
  <div class="w-80 md:w-1/2 p-5 max-sm:pt-36">
    <form @submit.prevent="submitForm">
      <!-- Steps Navigation -->
      <nav aria-label="Progress">
        <ol role="list" class="flex items-center justify-center">
          <li v-for="(step, stepIdx) in steps" :key="step.name" :class="[stepIdx !== steps.length - 1 ? 'pr-8 sm:pr-20' : '', 'relative']">
            <template v-if="step.status === 'complete'">
              <div class="absolute inset-0 flex items-center" aria-hidden="true">
                <div class="h-0.5 w-full bg-[#4683f7]"></div>
              </div>
              <a href="#" class="relative w-8 h-8 flex items-center justify-center bg-[#4683f7] rounded-full">
                <Icon name="mdi:check" class="w-5 h-5 text-white" aria-hidden="true" />
                <span class="sr-only">{{ step.name }}</span>
              </a>
            </template>
            <template v-else-if="step.status === 'current'">
              <div class="absolute inset-0 flex items-center" aria-hidden="true">
                <div class="h-0.5 w-full bg-gray-200"></div>
              </div>
              <a href="#" class="relative w-8 h-8 flex items-center justify-center bg-white border-2 border-[#4683f7] rounded-full" aria-current="step">
                <span class="h-2.5 w-2.5 bg-[#4683f7] rounded-full" aria-hidden="true"></span>
                <span class="sr-only">{{ step.name }}</span>
              </a>
            </template>
            <template v-else>
              <div class="absolute inset-0 flex items-center" aria-hidden="true">
                <div class="h-0.5 w-full bg-gray-200"></div>
              </div>
              <a href="#" class="group relative w-8 h-8 flex items-center justify-center bg-white border-2 border-gray-300 rounded-full hover:border-gray-400">
                <span class="h-2.5 w-2.5 bg-transparent rounded-full group-hover:bg-gray-300" aria-hidden="true"></span>
                <span class="sr-only">{{ step.name }}</span>
              </a>
            </template>
          </li>
        </ol>
      </nav>
      <transition name="fade" mode="out-in">
        <div :key="currentStep" class="flex flex-col justify-center">
          <div v-if="currentStep === 1">
            <h2 class="text-2xl my-5 text-center text-[#4683f7] font-bold">Personal Information</h2>
            <BaseInput
              icon="ic:baseline-person"
              type="text"
              placeholder="First Name"
              v-model="firstName"
              iconColor="text-[#4683f7]"
              borderColor="border-gray-300"
              focusBorderColor="focus:border-[#4683f7]"
              textColor="text-gray-900"
            />
            <BaseInput
              icon="ph:signature-bold"
              type="text"
              placeholder="Last Name"
              v-model="lastName"
              iconColor="text-[#4683f7]"
              borderColor="border-gray-300"
              focusBorderColor="focus:border-[#4683f7]"
              textColor="text-gray-900"
            />
          </div>
          <div v-if="currentStep === 2">
            <h2 class="text-2xl my-5 text-center text-[#4683f7] font-bold">Account Details</h2>
            <BaseInput
              icon="material-symbols:alternate-email"
              type="text"
              placeholder="Email"
              v-model="email"
              iconColor="text-[#4683f7]"
              borderColor="border-gray-300"
              focusBorderColor="focus:border-[#4683f7]"
              textColor="text-gray-900"
            />
            <URadioGroup v-model="user_type" legend="User type" :options="user_types" />




          </div>
          <div v-if="currentStep === 3">
            <h2 class="text-2xl my-5 text-center text-[#4683f7] font-bold">Security</h2>
            <BaseInput
              icon="teenyicons:password-outline"
              type="password"
              placeholder="Password"
              v-model="password"
              iconColor="text-[#4683f7]"
              borderColor="border-gray-300"
              focusBorderColor="focus:border-[#4683f7]"
              textColor="text-gray-900"
            />
            <BaseInput
              icon="teenyicons:password-outline"
              type="password"
              placeholder="Confirm Password"
              v-model="confirmPassword"
              iconColor="text-[#4683f7]"
              borderColor="border-gray-300"
              focusBorderColor="focus:border-[#4683f7]"
              textColor="text-gray-900"
            />
          </div>
        </div>
      </transition>
      <div class="flex gap-2 justify-between mt-5">
        <button type="button" class="w-full py-3 px-5 bg-[#4683f7] text-white font-bold rounded-lg shadow-lg hover:bg-[#3a6fd0] transition transform hover:scale-105" @click="prevStep" v-if="currentStep > 1">
          Previous
        </button>
        <button type="button" class="w-full py-3 px-5 bg-[#4683f7] text-white font-bold rounded-lg shadow-lg hover:bg-[#3a6fd0] transition transform hover:scale-105" @click="nextStep" v-if="currentStep < 3">
          Next
        </button>
        <button type="submit" class="w-full py-3 px-5 bg-[#4683f7] text-white font-bold rounded-lg shadow-lg hover:bg-[#3a6fd0] transition transform hover:scale-105" v-if="currentStep === 3">
          Sign Up
        </button>
      </div>
    </form>

    <!-- Divider -->
    <div class="flex items-center justify-center w-full my-5">
      <div class="h-px bg-gray-300 flex-grow"></div>
      <span class="mx-4 text-gray-600">or</span>
      <div class="h-px bg-gray-300 flex-grow"></div>
    </div>

    <div class="flex flex-col items-center mt-5">
      <nuxt-link to="/" class="flex items-center bg-white py-3 px-3 rounded-full border text-gray-700">
        <Icon name="ion:home" />
      </nuxt-link>
      <p class="mt-3 mb-1 text-gray-600">Already have an account?</p>
      <a @click="$emit('switch-to-login')" class="text-[#4683f7] font-bold cursor-pointer">Log In</a>
    </div>
  </div>
</template>

<script setup>
const { signUp } = useAuth()
const toast = useToast()

const user_types = [{
  value: 1,
  label: 'Customer'
}, {
  value: 2,
  label: 'Host'
}]

const currentStep = ref(1);
const steps = ref([
  { name: 'Step 1', status: 'current' },
  { name: 'Step 2', status: 'upcoming' },
  { name: 'Step 3', status: 'upcoming' },
]);

const firstName = ref('');
const lastName = ref('');
const email = ref('');
const password = ref('');
const user_type = ref(1)

const confirmPassword = ref('');

function nextStep() {
  if (currentStep.value < 3) {
    currentStep.value++;
    updateSteps();
  }
}

function prevStep() {
  if (currentStep.value > 1) {
    currentStep.value--;
    updateSteps();
  }
}

function updateSteps() {
  steps.value.forEach((step, index) => {
    if (index < currentStep.value - 1) {
      step.status = 'complete';
    } else if (index === currentStep.value - 1) {
      step.status = 'current';
    } else {
      step.status = 'upcoming';
    }
  });
}

const submitForm = async () => {
  if (password.value !== confirmPassword.value) {
		toast.add({
			title: 'Password do not match!',
			icon: 'i-heroicons-x-circle',
			color: 'red'
		})
    return;
  }

	const data = {
    fullname: `${firstName.value} ${lastName.value}`,
    email: email.value,
    password: password.value,
    user_type: user_type.value
	}
	// we can add a .then() if we wanna do something if logged in
	await signUp(data,{ callbackUrl: '/profile', redirect: true }).catch((err) => {
		error.value = err.data.detail[0];
	})
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
