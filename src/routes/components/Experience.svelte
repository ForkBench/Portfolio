<script>
	import { Badge, Timeline, TimelineItem } from 'flowbite-svelte';
	import { BuildingSolid } from 'flowbite-svelte-icons';
</script>

<Timeline order="vertical">
	<TimelineItem title="CERN (Internship)" date="March 2025 - September 2025">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-green-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-green-500 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<Badge class="rounded-md bg-blue-500 px-2 py-1 text-xs text-white hover:bg-blue-400">
			<div class="flex items-center space-x-1.5">JWT</div>
		</Badge>
		<Badge class="rounded-md bg-yellow-400 px-2 py-1 text-xs text-white hover:bg-yellow-300">
			<div class="flex items-center space-x-1.5">Python</div>
		</Badge>
		<Badge class="rounded-md bg-green-500 px-2 py-1 text-xs text-white hover:bg-green-400">
			<div class="flex items-center space-x-1.5">RESTful APIs</div>
		</Badge>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			I am thrilled to have the opportunity to work at <a
				href="https://home.cern.ch"
				target="_blank"
				class="italic"><b>CERN</b></a
			>, the <b>European Organization for Nuclear Research</b>. I will be working on
			<a href="https://github.com/DIRACGrid/diracx"><b><i>DiracX</i></b></a>, a project that aims to
			improve the performance of the Dirac software, which is used to manage the computing resources
			of the LHCb experiment. I am looking forward to contributing to this exciting project and
			learning from the talented team at CERN.
		</p>

		<p class="text-base font-normal text-gray-500 dark:text-gray-400">
			My main tasks will include:
		</p>

		<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
			<li>Develop the Pilot Code</li>
			<li>Assist in developing RESTful APIs, like implementing JWT authentication</li>
			<li>Contributing to clear, maintainable documentation</li>
		</ul>
	</TimelineItem>
	<TimelineItem title="Inseki (Personal Project)" date="July 2024 - Now">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-green-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-green-500 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<Badge class="rounded-md bg-blue-500 px-2 py-1 text-xs text-white hover:bg-blue-400">
			<div class="flex items-center space-x-1.5">Golang</div>
		</Badge>
		<Badge class="rounded-md bg-blue-400 px-2 py-1 text-xs text-white hover:bg-blue-300">
			<div class="flex items-center space-x-1.5">Go routines</div>
		</Badge>
		<Badge class="rounded-md bg-green-500 px-2 py-1 text-xs text-white hover:bg-green-400">
			<div class="flex items-center space-x-1.5">Optimizations</div>
		</Badge>
		<Badge class="rounded-md bg-green-600 px-2 py-1 text-xs text-white hover:bg-green-500">
			<div class="flex items-center space-x-1.5">Data Structures</div>
		</Badge>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			<a href="https://github.com/ForkBench/Inseki-Core"><i><b>Inseki</b></i></a> is an open-source tool
			that analyzes a disk to identify different projects, and is currently in development.
		</p>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			It was designed because, as a student, I often found myself with a lot of projects on my
			computer and I wanted a way to organize them. Inseki scans a disk and identifies different
			projects based on the project architecture. I am excited to continue working on this project
			and to share it with the community.
		</p>

		<p class="text-base font-normal text-gray-500 dark:text-gray-400">The technologies used are:</p>

		<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
			<li>For the core:</li>
			<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
				<li>Golang</li>
				<li>Go routines</li>
			</ul>
			<li>For the desktop app:</li>
			<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
				<li>WailsV3 (A Go library)</li>
				<li>HTMX (A JavaScript library)</li>
				<li>Templ (A Go template engine)</li>
			</ul>
		</ul>
	</TimelineItem>
	<TimelineItem title="Smart Sorter (Personal Project)" date="July 2022 - July 2024">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-green-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-green-500 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<Badge class="rounded-md bg-yellow-400 px-2 py-1 text-xs text-white hover:bg-yellow-300">
			<div class="flex items-center space-x-1.5">JavaScript</div>
		</Badge>
		<Badge class="rounded-md bg-green-500 px-2 py-1 text-xs text-white hover:bg-green-400">
			<div class="flex items-center space-x-1.5">NodeJS</div>
		</Badge>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			<a href="https://github.com/ForkBench/Smart-Sorter"><i><b>Smart Sorter</b></i></a> is the original
			project behind Inseki. It is an open-source tool that sorts files based on their type.
		</p>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			This original version was written in <u>JavaScript</u>, and I decided to rewrite it in
			<u>Golang</u> to improve its performance and to learn more about the language.
		</p>
	</TimelineItem>
	<TimelineItem title="Astro' (Personal Project)" date="June 2024 - Now">
		<svelte:fragment slot="icon">
			<span
				class="absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full bg-green-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
			>
				<BuildingSolid class="h-4 w-4 text-green-500 dark:text-primary-400" />
			</span>
		</svelte:fragment>
		<Badge class="rounded-md bg-blue-500 px-2 py-1 text-xs text-white hover:bg-blue-400">
			<div class="flex items-center space-x-1.5">Golang</div>
		</Badge>
		<Badge class="rounded-md bg-gray-400 px-2 py-1 text-xs text-white hover:bg-gray-300">
			<div class="flex items-center space-x-1.5">Databases</div>
		</Badge>
		<Badge class="rounded-md bg-red-500 px-2 py-1 text-xs text-white hover:bg-red-400">
			<div class="flex items-center space-x-1.5">Svelte</div>
		</Badge>
		<Badge class="rounded-md bg-green-500 px-2 py-1 text-xs text-white hover:bg-green-400">
			<div class="flex items-center space-x-1.5">Data Structures</div>
		</Badge>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			<a href="https://github.com/ForkBench/AstroProject"><i><b>Astro'</b></i></a> is a project that
			aims to create a competition management platform for fencing.
		</p>
		<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
			This project was born out of my passion for fencing and my desire to contribute to the fencing
			community. Furthermore, I want to create a modern and user-friendly platform that will make it
			easier for fencers to participate in competitions and for organizers to manage them.
		</p>

		<p class="text-base font-normal text-gray-500 dark:text-gray-400">The technologies used are:</p>

		<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
			<li>For the core:</li>
			<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
				<li>Golang</li>
				<li>Databases</li>
			</ul>
			<li>For the desktop app:</li>
			<ul class="mt-2 list-disc pl-8 text-gray-500 dark:text-gray-400">
				<li>WailsV3 (A Go library)</li>
				<li>Svelte (A JavaScript library)</li>
			</ul>
		</ul>
	</TimelineItem>
</Timeline>
