<template>
  <div class="mt-16">
        <!-- Hero Section -->
    <div class="banner rounded-b-[5%] text-white text-center py-20 w-full">
      <UContainer>
        <h2 class="uppercase tracking-wider text-lg md:text-xl text-gray-300">Achieving Success, One Milestone at a Time</h2>
        <h1 class="text-4xl my-8 md:text-6xl font-extrabold leading-tight">Our Vision</h1>
        <p class="text-md md:text-xl max-w-2xl mx-auto">Milestone is dedicated to helping store owners streamline their operations, manage inventory efficiently, and enhance customer engagement.</p>
      </UContainer>
    </div>

    <!-- About Section -->
    <UContainer>
      <div class="bg-[--sec-bg] p-10 my-10 rounded-3xl shadow grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="col-span-2 flex flex-col justify-center space-y-8">
          <div>
            <h2 class="text-2xl md:text-3xl font-bold mb-4">Empowering Store Owners</h2>
            <p class="text-md md:text-lg text-[--light-text]">Milestone provides a comprehensive management app designed to give store owners enhanced business insights, improve customer engagement, automate processes, and mitigate operational risks. Optimize productivity and acknowledge great work effortlessly.</p>
          </div>
          <div>
            <h2 class="text-2xl md:text-3xl font-bold mb-4">Building Stronger Teams</h2>
            <p class="text-md md:text-lg text-[--light-text]">At Milestone, we focus on creating strong teams by equipping store owners with tools to manage their staff effectively, ensuring they have the necessary experience and skills for success.</p>
          </div>
          <div>
            <h2 class="text-2xl md:text-3xl font-bold mb-4">Leading Management Solutions</h2>
            <p class="text-md md:text-lg text-[--light-text]">Milestone is a leader in management solutions for store owners. Whether it's inventory management, customer relationship management, or sales analytics, Milestone delivers top-notch solutions tailored to your needs.</p>
          </div>
        </div>
        <div class="col-span-1 flex flex-col items-center justify-center">
          <img class="w-48 h-48 object-cover shadow-lg" src="https://via.placeholder.com/300" alt="About Image">
        </div>
      </div>
    </UContainer>

    <!-- Team Section -->
    <UContainer>
      <div class="bg-[--sec-bg] p-10 my-10 rounded-3xl shadow text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 md:mb-16">Meet Our Team</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="flex flex-col items-center">
            <img class="w-24 h-24 md:w-48 md:h-48 object-cover rounded-full border-4 border-gray-200 shadow-lg" src="https://via.placeholder.com/200" alt="Arvin Moravej">
            <h3 class="text-xl md:text-2xl font-bold mt-4">Arvin Moravej</h3>
            <p class="text-md md:text-lg">Founder</p>
            <blockquote class="text-md md:text-lg italic px-4 md:px-20 mt-4 text-[--light-text]">"Our mission at Milestone is to revolutionize the way store owners manage their businesses, ensuring efficiency and growth."</blockquote>
          </div>
          <div class="flex flex-col items-center">
            <img class="w-24 h-24 md:w-48 md:h-48 object-cover rounded-full border-4 border-gray-200 shadow-lg" src="https://via.placeholder.com/200" alt="Kianmehr Haddad">
            <h3 class="text-xl md:text-2xl font-bold mt-4">Kianmehr Haddad</h3>
            <p class="text-md md:text-lg">Co-Founder</p>
            <blockquote class="text-md md:text-lg italic text-center px-4 md:px-20 mt-4 text-[--light-text]">"With Milestone, we're pushing the boundaries of technology to provide the best management solutions for store owners."</blockquote>
          </div>
        </div>
      </div>
    </UContainer>

    <!-- Contact Section -->
    <UContainer>
      <div class="bg-[--sec-bg] p-10 my-10 rounded-3xl shadow text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 md:mb-16">Contact Us</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-14">
          <div class="flex flex-col items-center">
            <h3 class="text-xl md:text-2xl font-bold mb-4">Head Office</h3>
            <p class="text-md md:text-lg">123 Business Rd, Suite 456<br>Business City, BC 78910</p>
          </div>
          <div class="flex flex-col items-center">
            <h3 class="text-xl md:text-2xl font-bold mb-4">Email</h3>
            <p class="text-md md:text-lg"><a href="mailto:info@milestone.com" class="text-blue-500">info@milestone.com</a></p>
          </div>
          <div class="flex flex-col items-center">
            <h3 class="text-xl md:text-2xl font-bold mb-4">Phone</h3>
            <p class="text-md md:text-lg">+1 (234) 567-890</p>
          </div>
        </div>
      </div>
    </UContainer>
</div>
</template>
