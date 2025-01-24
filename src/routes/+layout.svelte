<script lang="ts">
	import '../app.css';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';

	let { children } = $props();
</script>

<Navbar rounded color="red" class="w-4/5 m-auto mt-4">
	<NavBrand href="/">
		<img src="/Inseki.png" class="me-3 h-6 sm:h-9" alt="Logo" />
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Forkbench</span>
	</NavBrand>
	<NavHamburger />
	<NavUl>
		<NavLi href="/">Home</NavLi>
		<NavLi href="/projects">Projects</NavLi>
		<NavLi href="/about">About</NavLi>
		<NavLi href="/contact">Contact</NavLi>
	</NavUl>
</Navbar>

<main class="w-4/5 m-auto">
	{@render children()}
</main>

