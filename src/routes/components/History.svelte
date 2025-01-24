<script>
	import { Timeline, TimelineItem } from 'flowbite-svelte';
	import { BuildingSolid } from 'flowbite-svelte-icons';
</script>

<Timeline order="vertical">
	<TimelineItem title="ISIMA Computer Science School (Master)" date="2023 - Now">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-primary-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-orange-400 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			I am excited to have joined <b>ISIMA</b>, where I am specializing in <u>cybersecurity</u> and
			<u>networks</u>. This opportunity is allowing me to develop my skills in various areas such as
			<u>pentesting</u>, the <u>Internet of Things</u> (IoT), and <u>web security</u>, among others.
			I am thoroughly enjoying diving into these exciting topics and actively contributing to
			digital security.
		</p>
	</TimelineItem>
	<TimelineItem title="Prep'ISIMA (Bachelor)" date="2021 - 2023">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-primary-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-orange-400 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<p class="text-base font-normal text-gray-500 dark:text-gray-400">
			I went to <b>Clermont-Auvergne University</b> to prepare for the entrance to <b>ISIMA</b>.
			This experience allowed me to consolidate my knowledge in mathematics and computer science. I
			also had the opportunity to work on various projects, such as creating a
			<u>server in Java</u>, developing <u>games in C and Java</u>, and creating a
			<u>website in HTML, CSS, and JavaScript</u>.
		</p>
	</TimelineItem>
	<TimelineItem title="Maine de Biran High School (Baccalaureate)" date="2018 - 2021">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-primary-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-orange-400 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<p class="text-base font-normal text-gray-500 dark:text-gray-400">
			I graduated from <b>Maine de Biran High School</b> with a <u>scientific baccalaureate</u>.
			This diploma allowed me to develop my skills in mathematics, physics, and computer science.
		</p>
	</TimelineItem>
</Timeline>
