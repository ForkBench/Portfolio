<script lang="ts">
	import History from './components/History.svelte';
	import { Heading, P, Badge, Card, Button, Avatar } from 'flowbite-svelte';
	import {
		LinkedinSolid,
		GithubSolid,
		BuildingSolid,
		MailBoxSolid,
		LockSolid
	} from 'flowbite-svelte-icons';
	import Experience from './components/Experience.svelte';
</script>

<section
	id="top-section"
	class="flex h-screen flex-col items-center justify-center space-y-4 text-center"
>
	<Heading tag="h1" class="mb-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl"
		>Robin, student at ISIMA.</Heading
	>
	<P class="mb-6 text-lg text-slate-400 sm:px-16 lg:text-xl xl:px-48"
		>French student currently based in Clermont-Ferrand, studying computer science, cyber security
		and networking.</P
	>
	<div id="badge-container" class="flex flex-row items-center justify-center space-x-4">
		<Badge
			class="rounded-md bg-blue-500 px-4 py-2 text-white hover:bg-blue-400"
			href="https://www.linkedin.com/in/robin-van-de-merghel"
		>
			<div class="flex items-center space-x-1.5">
				<LinkedinSolid class="float-left me-1.5 h-2.5 w-2.5 text-white dark:text-primary-400" />
				Linkedin
			</div>
		</Badge>
		<Badge
			class="rounded-md bg-gray-800 px-4 py-2 text-white hover:bg-gray-600"
			href="https://github.com/ForkBench"
		>
			<div class="flex items-center space-x-1.5">
				<GithubSolid class="float-left me-1.5 h-2.5 w-2.5 text-white dark:text-primary-400" />
				Github
			</div>
		</Badge>
		<Badge
			class="rounded-md bg-orange-400 px-4 py-2 text-white hover:bg-orange-300"
			href="https://www.isima.fr/en/home/"
		>
			<div class="flex items-center space-x-1.5">
				<BuildingSolid class="float-left me-1.5 h-2.5 w-2.5 text-white dark:text-primary-400" />
				ISIMA
			</div>
		</Badge>
	</div>
</section>

<section
	id="experience-section"
	class="flex min-h-screen flex-col items-center justify-center space-y-4"
>
	<Heading
		tag="h1"
		class="mb-4 text-center"
		customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Experience</Heading
	>
	<div id="container" class="flex max-w-6xl flex-col items-center justify-center space-y-4">
		<Experience />
	</div>
</section>

<section
	id="education-section"
	class="flex min-h-screen flex-col items-center justify-center space-y-4"
>
	<Heading
		tag="h1"
		class="mb-4 text-center"
		customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Education</Heading
	>
	<div id="container" class="flex max-w-6xl flex-col items-center justify-center space-y-4">
		<History />
	</div>
</section>

<section
	id="hobbies-section"
	class="flex min-h-screen flex-col items-center justify-center space-y-4"
>
	<Heading
		tag="h1"
		class="mb-4 text-center"
		customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Hobbies</Heading
	>

	<div class="space-y-4">
		<Card img="/Fencing.JPG" horizontal size="md" class="mt-6 max-w-4xl space-y-4">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Fencing</h5>
			<p class="mb-3 text-justify font-normal leading-tight text-gray-500 dark:text-gray-400">
				It has been now sixteen years since I started fencing.
			</p>
			<p class="mb-3 text-justify font-normal leading-tight text-gray-500 dark:text-gray-400">
				I have been practicing foil in competition for almost fourteen years, and was able to
				participate to two world cups, and nearly ten national championships. I also obtained my
				referee diploma and am now a regional referee.
			</p>
		</Card>
		<Card img="/Photography.JPG" horizontal size="md" class="mt-6 max-w-4xl space-y-4">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
				Photography
			</h5>
			<p class="mb-3 text-justify font-normal leading-tight text-gray-500 dark:text-gray-400">
				In addition to fencing, I have been practicing photography for about five years.
			</p>
			<p class="mb-3 text-justify font-normal leading-tight text-gray-500 dark:text-gray-400">
				I started astrophotography with a Canon EOS 600D, acquired a telescope (a 150/750 from
				Skywatcher) with a motorized mount (EQ3-2) and developed my skills in post-processing with
				software such as DeepSkyStacker and Photoshop.
			</p>
			<p class="mb-3 text-justify font-normal leading-tight text-gray-500 dark:text-gray-400">
				A few years later, I joined my passion for fencing and photography by taking pictures during
				fencing competitions, and had the chance to have some of my photos published on some french
				Instagram accounts.
			</p>

			<!--
            <Button color="light" class="dark:text-white" href="/gallery">
                <FileImageSolid class="w-5 h-5 me-1.5" />
                Discover my gallery
            </Button>
            -->
		</Card>
	</div>
</section>

<section id="contact-section" class="flex h-screen flex-col items-center justify-center space-y-4">
	<Heading
		tag="h1"
		class="mb-4 text-center"
		customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Contacts</Heading
	>
	<Card padding="md" class="mx-auto max-w-sm">
		<div class="flex flex-col items-center pb-4">
			<Avatar size="lg" src="/Portrait.JPG" />
			<h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">Robin Van de Merghel</h5>
			<span class="text-sm text-gray-500 dark:text-gray-400">Cybersecurity Student</span>
			<span class="mt-2 text-justify text-sm text-gray-500 dark:text-gray-400">
				I am open to new opportunities and collaborations. Feel free to reach out to me if you have
				any questions or would like to connect.
			</span>
			<div class="mt-4 flex space-x-3 lg:mt-6 rtl:space-x-reverse">
				<Button href="/public/public_key.asc">
					<LockSolid class="me-1.5 h-5 w-5" />
					Get my PGP key
				</Button>
				<Button color="light" class="dark:text-white" href="mailto:forkbench@proton.me">
					<MailBoxSolid class="me-1.5 h-5 w-5" />
					Mail me
				</Button>
			</div>
		</div>
	</Card>
</section>
