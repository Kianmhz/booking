<template>
    <div class="relative mb-5">
      <Icon :name="icon" class="absolute top-3 left-2" :class="iconClass" />
      <input
        :type="type"
        class="w-full bg-transparent border-b-2 pl-8 py-2 font-bold focus:outline-none placeholder-gray-500"
        :class="inputClass"
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
      />
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    icon: {
      type: String,
      default: 'material-symbols:account-circle-full'
    },
    type: {
      type: String,
      default: 'text'
    },
    placeholder: {
      type: String,
      default: 'Username / Email'
    },
    modelValue: {
      type: String,
      default: ''
    },
    iconColor: {
      type: String,
      default: 'text-purple-400'
    },
    borderColor: {
      type: String,
      default: 'border-purple-300'
    },
    focusBorderColor: {
      type: String,
      default: 'focus:border-purple-500'
    },
    textColor: {
      type: String,
      default: 'text-gray-900'
    }
  });
  
  const emit = defineEmits(['update:modelValue']);
  
  const iconClass = computed(() => props.iconColor);
  const inputClass = computed(() => `${props.borderColor} ${props.focusBorderColor} ${props.textColor}`);
  </script>