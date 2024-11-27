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
            <PropertyStars v-model="reviewForm.rating" />
            <UTextarea
              placeholder="Write your review here"
              v-model="reviewForm.review"
              required
            ></UTextarea>
            <UButton
              type="submit"
              @click="sendReview()"
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

      <!-- Reviews{{ allReviews }} -->
      <div class="sm:col-span-5">
        <div class="divide-y divide-[--border]">
          <div
            v-for="review in allReviews"
            :key="review.id"
            class="py-12 first:pt-0"
          >
            <div class="flex items-center">
              <div>
                <h4 class="text-sm font-bold text-[--text]">Guest</h4>
                <div class="mt-1 flex items-center">

                  <Icon
                    v-for="rating in [0, 1, 2, 3, 4]"
                    size="16"
                    :key="rating"
                    :name="review.rating > rating ? 'ion:star' : 'ion:star-outline'"
                    :class="[review.rating > rating ? 'text-[--main-special]' : 'text-[--light-text]', 'flex-shrink-0']"
                    aria-hidden="true"
                  />
                </div>
              </div>
            </div>
            <div
              class="mt-4 space-y-6 text-base italic text-[--light-text]"
              v-html="review.body"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const {id} = defineProps(['id'])
const exploreStore = useExplore()
const toast = useToast();
const allReviews = ref([])
allReviews.value = await exploreStore.getReviews(id)

const sendReview = async () => {
  const reviewData = {
    review_property: id,
    rating: reviewForm.value.rating,
    body: reviewForm.value.review,
  }
  console.log(reviewData);
  const response = await exploreStore.sendReview(reviewData)
  if (response) {
    toast.add({
      title: 'Review submitted',
      description: 'Thank you for sharing your thoughts!',
      status: 'success',
    });
    allReviews.value = await exploreStore.getReviews(id)
  }
  else {
    toast.add({
      title: 'Failed to submit review',
      description: 'Please try again later.',
      status: 'error',
    });
  }
};

const isOpen = ref(false);

const reviewForm = ref({
  rating: 0,
  review: ''
});


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
    },

  ],
};
</script>
