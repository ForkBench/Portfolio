<script lang="ts">
	import { Gallery, Heading } from 'flowbite-svelte';
	const images1 = [
		{ alt: 'Fencing Competition', src: '/gallery/fencing-1.JPEG' },
		{ alt: 'Fencing Competition', src: '/gallery/fencing-2.JPG' }
	];
	const images2 = [
		{ alt: 'Fencing Competition', src: '/gallery/fencing-4.JPG' },
		{ alt: 'Fencing Competition', src: '/gallery/fencing-5.JPEG' }
	];
	const images3 = [
		{ alt: 'Fencing Competition', src: '/gallery/fencing-7.JPG' },
		{ alt: 'Fencing Competition', src: '/gallery/fencing-6.JPEG' }
	];
	const images4 = [
		{ alt: 'Fencing Competition', src: '/gallery/fencing-10.JPG' },
		{ alt: 'Fencing Competition', src: '/gallery/fencing-9.PNG' }
	];
</script>

<section
	id="gallery"
	class="flex flex-col items-center justify-center space-y-4 text-center min-h-screen h-auto"
>
	<Heading tag="h1" class="m-5">Here is a quick look at my work.</Heading>

	<Gallery class="grid-cols-2 gap-4 md:grid-cols-4">
		<Gallery items={images1} />
		<Gallery items={images2} />
		<Gallery items={images3} />
		<Gallery items={images4} />
	</Gallery>
</section>
