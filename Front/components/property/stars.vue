<template>
    <div class="flex items-center">
      <span
        v-for="rating in 5"
        :key="rating"
        @click="setRating(rating)"
        @mouseover="hoverRating = rating"
        @mouseleave="hoverRating = 0"
        :class="[
          rating <= (hoverRating || modelValue) ? 'text-[--main-special]' : 'text-[--light-text]',
          'px-1 cursor-pointer transition-all hover:scale-125'
        ]"
      >
      <Icon :name="rating <= (hoverRating || modelValue) ? 'ion:star' : 'ion:star-outline'" aria-hidden="true" size="25"/>
      </span>
    </div>
</template>
  
<script setup>
  const props = defineProps({
    modelValue: {
      type: Number,
      default: 0
    }
  });
  const emit = defineEmits(['update:modelValue']);
  
  const hoverRating = ref(0);
  
  const setRating = (rating) => {
    emit('update:modelValue', rating);
  };
  
  watch(() => props.modelValue, (newValue) => {
    hoverRating.value = newValue;
  });
</script>
  