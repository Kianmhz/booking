<template>
  <div class="bg-[--sec-bg] p-10 rounded-3xl shadow">
    <h2 class="text-2xl font-bold mb-4">Recent reviews</h2>
    <div class="grid grid-cols-1 sm:grid-cols-7 gap-16">
      <!-- Review summary -->
      <div class="sm:col-span-2">
        <div class="flex items-center">
          <div>
            <div class="flex items-center">
              <Icon
                v-for="rating in [0, 1, 2, 3, 4]"
                :key="rating"
                size="16"
                :name="reviews.average > rating ? 'ion:star' : 'ion:star-outline'"
                :class="[reviews.average > rating ? 'text-[--main-special]' : 'text-[--light-text]', 'flex-shrink-0']"
                aria-hidden="true"
              />
            </div>
            <p class="sr-only">{{ reviews.average }} out of 5 stars</p>
          </div>
          <p class="ml-2 text-sm text-[--light-text]">Based on {{ reviews.totalCount }} reviews</p>
        </div>

        <!-- Review ratings -->
        <div class="mt-6">
          <dl class="space-y-4">
            <div
              v-for="count in reviews.counts"
              :key="count.rating"
              class="flex items-center text-sm"
            >
              <dt class="flex-1 flex items-center">
                <p class="w-4 font-medium text-[--light-text]">
                  {{ count.rating }}<span class="sr-only"> star reviews</span>
                </p>
                <div aria-hidden="true" class="ml-2 flex-1 flex items-center">
                  <Icon name="ion:star" class="text-[--main-special]" size="16"/>
                  <div class="ml-3 relative flex-1">
                    <UMeter :value="(count.count / reviews.totalCount) * 100" />
                  </div>
                </div>
              </dt>
              <dd class="ml-3 w-10 text-right tabular-nums text-sm text-[--light-text]">
                {{ Math.round((count.count / reviews.totalCount) * 100) }}%
              </dd>
            </div>
          </dl>
        </div>

        <!-- Add Review -->
        <UButton
          @click="isOpen = true"
          variant="outline"
          block
          :ui="{ rounded: 'rounded-full' }"
          class="mt-6"
          >
          Write a Review
        </UButton>
        <UModal v-model="isOpen">
          <form class="w-full p-10 mx-auto space-y-4" @submit.prevent="submitReview">
            <h1>Share your thoughts</h1>
            <StoreStars v-model="reviewForm.rating" />
            <UInput
              type="text"
              placeholder="Name"
              v-model="reviewForm.name"
              required
            />
            <UInput
              type="email"
              placeholder="Email"
              v-model="reviewForm.email"
              required
            />
            <UTextarea
              placeholder="Write your review here"
              v-model="reviewForm.review"
              required
            ></UTextarea>
            <UButton
              type="submit"
              variant="outline"
              block
              :ui="{ rounded: 'rounded-full' }"
            >
              <Icon name="line-md:telegram"/>
              Submit Review
            </UButton>
          </form>
        </UModal>
      </div>

      <!-- Reviews -->
      <div class="sm:col-span-5">
        <div class="divide-y divide-[--border]">
          <div
            v-for="review in reviews.featured"
            :key="review.id"
            class="py-12 first:pt-0"
          >
            <div class="flex items-center">
              <img
                :src="review.avatarSrc"
                :alt="`${review.author}.`"
                class="h-12 w-12 rounded-full"
              />
              <div class="ml-4">
                <h4 class="text-sm font-bold text-[--text]">{{ review.author }}</h4>
                <div class="mt-1 flex items-center">
                  <Icon
                    v-for="rating in [0, 1, 2, 3, 4]"
                    size="16"
                    :key="rating"
                    :name="reviews.average > rating ? 'ion:star' : 'ion:star-outline'"
                    :class="[reviews.average > rating ? 'text-[--main-special]' : 'text-[--light-text]', 'flex-shrink-0']"
                    aria-hidden="true"
                  />
                </div>
              </div>
            </div>
            <div
              class="mt-4 space-y-6 text-base italic text-[--light-text]"
              v-html="review.content"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

const isOpen = ref(false);

const reviewForm = ref({
  name: '',
  email: '',
  rating: 0,
  review: ''
});

const submitReview = () => {
  // Handle the review submission logic here
  console.log(reviewForm.value);
  isOpen.value = false;
};

const reviews = {
  average: 4,
  totalCount: 1624,
  counts: [
    { rating: 5, count: 1019 },
    { rating: 4, count: 162 },
    { rating: 3, count: 97 },
    { rating: 2, count: 199 },
    { rating: 1, count: 147 },
  ],
  featured: [
    {
      id: 1,
      rating: 5,
      content: `
        <p>Absolutely loved it!</p>
      `,
      author: "Emily Selman",
      avatarSrc:
        "https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80",
    },
    
  ],
};
</script>
