<script setup>
import { ref, watch } from 'vue';
import { format, parseISO, isValid, differenceInCalendarDays } from 'date-fns';

const toast = useToast();

// Mock data for unavailable dates
const unavailableDates = ['2024-11-25', '2024-11-26', '2024-12-01'].map((date) => new Date(date));

// Reactive states
const checkInDate = ref(null); // Use `null` as initial value to satisfy `Date` type requirement
const checkOutDate = ref(null);
const totalPrice = ref(0);

// Room pricing
const pricePerNight = 100;

// Function to calculate the total price
const calculateTotalPrice = () => {
  if (checkInDate.value && checkOutDate.value) {
    const nights = differenceInCalendarDays(checkOutDate.value, checkInDate.value);
    totalPrice.value = nights > 0 ? nights * pricePerNight : 0;
  } else {
    totalPrice.value = 0;
  }
};

// Watch for changes in check-in or check-out dates
watch([checkInDate, checkOutDate], calculateTotalPrice);

// Function to check if a date is unavailable
const isDateUnavailable = (date) =>
  unavailableDates.some((unavailableDate) => unavailableDate.getTime() === date.getTime());

// Booking logic
const bookRoom = () => {
  if (!checkInDate.value || !checkOutDate.value) {
    toast.add({ title: 'Please select both check-in and check-out dates.', type: 'warning' });
    return;
  }

  if (checkOutDate.value <= checkInDate.value) {
    toast.add({ title: 'Check-out date must be after the check-in date.', type: 'error' });
    return;
  }

  for (let date = new Date(checkInDate.value); date < checkOutDate.value; date.setDate(date.getDate() + 1)) {
    if (isDateUnavailable(date)) {
      toast.add({ title: 'Selected dates include unavailable periods.', type: 'error' });
      return;
    }
  }

  toast.add({
    title: `Booking confirmed from ${format(checkInDate.value, 'yyyy-MM-dd')} to ${format(
      checkOutDate.value,
      'yyyy-MM-dd'
    )}. Total: $${totalPrice.value}`,
    type: 'success',
  });
};
</script>

<template>
  <div class="mx-auto my-10 max-w-4xl p-8 bg-[--sec-bg] rounded-3xl shadow">
    <h2 class="text-2xl font-bold mb-6">Book Your Stay</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Left Column: Check-In and Check-Out Dates -->
      <div class="flex flex-col gap-6">
        <div>
          <label for="check-in" class="block mb-2 text-[--text] font-medium">Check-In Date</label>
          <UPopover :popper="{ placement: 'bottom-start' }">
            <UButton
              icon="i-heroicons-calendar-days-20-solid"
              :label="checkInDate ? format(checkInDate, 'd MMM, yyyy') : 'Select Date'"
            />
            <template #panel="{ close }">
              <DatePicker
                v-model="checkInDate"
                :disabled-dates="unavailableDates"
                is-required
                @close="close"
              />
            </template>
          </UPopover>
        </div>
        <div>
          <label for="check-out" class="block mb-2 text-[--text] font-medium">Check-Out Date</label>
          <UPopover :popper="{ placement: 'bottom-start' }">
            <UButton
              icon="i-heroicons-calendar-days-20-solid"
              :label="checkOutDate ? format(checkOutDate, 'd MMM, yyyy') : 'Select Date'"
            />
            <template #panel="{ close }">
              <DatePicker
                v-model="checkOutDate"
                :disabled-dates="unavailableDates"
                is-required
                @close="close"
              />
            </template>
          </UPopover>
        </div>
      </div>

      <!-- Right Column: Price and Booking Button -->
      <div class="flex flex-col justify-between">
        <div>
          <p class="text-lg">
            Price per night: <span class="font-bold">$100</span>
          </p>
          <p v-if="totalPrice > 0" class="text-lg mt-4">
            Total Price: <span class="font-bold">${{ totalPrice }}</span>
          </p>
        </div>
        <UButton
          class="p-4"
          @click="bookRoom"
        >
          Confirm Booking
        </UButton>
      </div>
    </div>
  </div>
</template>
