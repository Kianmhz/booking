<template>
  <h1 class="text-3xl font-bold mb-4">Frequently Asked Questions</h1>
  <p class="text-[--light-text] mb-8">
    Welcome to the Milestone FAQ. Here you’ll find answers to the most common questions about booking, hosting, and using our platform.
  </p>
  <div v-for="(faq, index) in faqs" :key="index" class="mb-4">
    <h2 @click="toggle(index)" class="text-lg border-b border-[--border] pb-3 font-semibold text-[--main-special] cursor-pointer">
      {{ faq.question }}
    </h2>
    <transition-expand>
      <p v-if="faq.open" class="text-[--light-text] mt-2">
        {{ faq.answer }}
      </p>
    </transition-expand>
  </div>
</template>

<script setup>
const faqs = ref([
  {
    question: 'How do I book a stay?',
    answer: 'To book a stay, browse our listings, select your preferred property, and complete the booking process by following the on-screen instructions.',
    open: false,
  },
  {
    question: 'What are the payment options?',
    answer: 'We accept major credit/debit cards, PayPal, and other popular payment methods to make your booking process seamless.',
    open: false,
  },
  {
    question: 'How do I contact a host?',
    answer: 'You can message the host directly through the Milestone platform once you’ve found a listing you’re interested in.',
    open: false,
  },
  {
    question: 'What is the cancellation policy?',
    answer: 'Each listing has its own cancellation policy. Please review the policy on the listing page before booking.',
    open: false,
  },
  {
    question: 'How can I become a host?',
    answer: 'To become a host, sign up on Milestone and complete the hosting application. Once approved, you can start listing your properties.',
    open: false,
  },
]);

const toggle = (index) => {
  faqs.value[index].open = !faqs.value[index].open;
};
</script>