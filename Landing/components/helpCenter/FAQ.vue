<template>
      <h1 class="text-3xl font-bold mb-4">Frequently Asked Questions</h1>
      <p class="text-[--light-text] mb-8">
        Welcome to our FAQ section. Here you will find answers to the most common questions about our services and offerings.
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
    question: 'Where can I watch?',
    answer: 'You can watch our content on our website, mobile app, or through our partner platforms. Just log in with your account and start streaming!',
    open: false
  },
  {
    question: 'How do I subscribe?',
    answer: 'To subscribe, visit our subscription page and choose a plan that suits you. Follow the instructions to create an account and complete the payment process.',
    open: false
  },
  {
    question: 'What payment methods do you accept?',
    answer: 'We accept various payment methods including credit/debit cards, PayPal, and other popular online payment options.',
    open: false
  },
  {
    question: 'How can I contact support?',
    answer: 'If you need assistance, you can contact our support team through the Contact Support section on our website or by emailing support@example.com.',
    open: false
  }
]);

const toggle = (index) => {
  faqs.value[index].open = !faqs.value[index].open;
};
</script>