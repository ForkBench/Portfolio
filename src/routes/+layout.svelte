<script lang="ts">
	import '../app.css';
	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Footer,
		FooterCopyright,
		FooterBrand,
		FooterIcon
	} from 'flowbite-svelte';
	import { LinkedinSolid, GithubSolid, BuildingSolid } from 'flowbite-svelte-icons';

	let { children } = $props();
</script>

<Navbar rounded class="m-auto mt-4 w-4/5 bg-gray-100">
	<NavBrand href="/">
		<img src="/Inseki.png" class="me-3 h-6 sm:h-9" alt="Logo" />
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"
			>Forkbench</span
		>
	</NavBrand>
	<NavHamburger />
	<NavUl>
		<NavLi href="/" id="li1">Home</NavLi>
		<NavLi href="/gallery" id="li2">Gallery</NavLi>
		<NavLi href="/#contact" id="li4">Contact</NavLi>
	</NavUl>
</Navbar>

<main class="m-auto w-4/5">
	{@render children()}
</main>

<Footer footerType="socialmedia">
	<div class="md:flex md:justify-between">
		<div class="mb-6 md:mb-0">
			<FooterBrand
				href="https://flowbite.com"
				src="/Inseki.png"
				alt="Forkbench Logo"
				name="Forkbench"
			/>
		</div>
	</div>
	<hr class="my-6 border-gray-200 sm:mx-auto lg:my-8 dark:border-gray-700" />
	<div class="sm:flex sm:items-center sm:justify-between">
		<FooterCopyright href="/" by="Forkbench" />
		<div class="mt-4 flex space-x-6 sm:mt-0 sm:justify-center rtl:space-x-reverse">
			<FooterIcon href="https://github.com/forkbench">
				<GithubSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<FooterIcon href="https://www.linkedin.com/in/robin-van-de-merghel/">
				<LinkedinSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<FooterIcon href="https://isima.fr">
				<BuildingSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
		</div>
	</div>
</Footer>
