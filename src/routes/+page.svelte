<script lang="ts">
	import buttonImg from '$lib/images/button.png';
	import linkImg from '$lib/images/link.png';
	import Component from '../components/Component.svelte';

	type Item = {
		name: string;
		description: string;
		path: string;
		image: string;
	};

	const items: Item[] = [
		{
			name: 'Button',
			description: 'Button style with a nice little detail to improve your buttons!',
			path: '/components/button',
			image: buttonImg
		},
		{
			name: 'Link',
			description: 'Button style with a nice little detail to improve your buttons!',
			path: '/components/link',
			image: linkImg
		},
	];
</script>

<svelte:head>
	<title>SVELTE-UI</title>
	<meta name="description" content="Svelte UI Framework" />
</svelte:head>

<section class="w-full max-w-[800px]">
	{#each items as item}
		<Component {item} />
	{/each}
</section>

<style>
	section {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		gap: 0.5rem;
		justify-content: center;
		align-items: center;
		align-content: start;
	}
</style>
