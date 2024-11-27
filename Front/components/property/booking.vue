<script setup>
import { format, differenceInCalendarDays } from 'date-fns';

const toast = useToast();
const bookingStore = useBooking()
const exploreStore = useExplore()

const {id} = defineProps(['id'])

// Mock data for unavailable dates
const reservedDates = await bookingStore.getBooking(id);

const unavailableDates = [];
reservedDates.forEach((reservation) => {
  const start = new Date(reservation.check_in);
  const end = new Date(reservation.check_out);

  start.setHours(0, 0, 0, 0);
  end.setHours(0, 0, 0, 0);

  for (let date = new Date(start); date <= end; date.setDate(date.getDate() + 1)) {
    unavailableDates.push(new Date(date)); // Clone to avoid mutation
  }
});

// Reactive states
const checkInDate = ref(null); // Use `null` as initial value to satisfy `Date` type requirement
const checkOutDate = ref(null);
const totalPrice = ref(0);

// Room pricing
const priceresult = await exploreStore.getSingleExplore(id);
const pricePerNight = priceresult.price;

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
const bookRoom = async () => {
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


  const checkInDateST = checkInDate.value.toISOString().split('T')[0]
  const checkOutDateST = checkOutDate.value.toISOString().split('T')[0]
  const booking_data = {
    "booking_property": id,
    "check_in": checkInDateST,
    "check_out": checkOutDateST
  }
  const res = await bookingStore.addBooking(booking_data)
  console.log(res);
  if (res) {
    toast.add({
      title: `Booking confirmed from ${checkInDateST} to ${checkOutDateST}. Total: $${totalPrice.value}`,
      type: 'success',
    });
  }else {
    toast.add({
      title: 'Failed to book property',
      type: 'error'
    });
  }

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
            Price per night: <span class="font-bold">$ {{ pricePerNight }} </span>
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
