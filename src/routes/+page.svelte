<script lang="ts">
	import buttonImg from '$lib/images/button.png';
	import linkImg from '$lib/images/link.png';
	import cardImg from '$lib/images/card.png';
	import Component from '../components/Component.svelte';
	import { onMount } from 'svelte';

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
			description: 'Link style with a subtle underline and smooth hover animation!',
			path: '/components/link',
			image: linkImg
		},
		{
			name: 'Card Component',
			description: 'Button style with a nice little detail to improve your buttons!',
			path: '/components/card',
			image: cardImg
		}
	];

	let query = '';
	let filtered: Item[] = items;
	onMount(() => {
		const inputEl = document.querySelector<HTMLInputElement>(
			'input[placeholder="Search the svelte ui framework..."]'
		);
		if (!inputEl) return;

		const update = () => {
			query = inputEl.value;
			const q = query.trim().toLowerCase();
			filtered = q ? items.filter((i) => i.name.toLowerCase().includes(q)) : items;
		};

		inputEl.addEventListener('input', update);
		update();

		return () => inputEl.removeEventListener('input', update);
	});
</script>

<svelte:head>
	<title>SVELTE-UI</title>
	<meta name="description" content="Svelte UI Framework" />
</svelte:head>

<section class="w-full max-w-[800px]">
	<div style="width:100%; display:flex; justify-content:center;">
		<input
			type="text"
			style="width: 100%;max-width: 800px;"
			placeholder="Search the svelte ui framework..." />
	</div>
	{#each filtered as item}
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
		align-items: start;
		align-content: start;
	}
	input {
		background-color: #232329;
		border-radius: 5px;
		border: 1px #454551 solid;
		color: #fff3e9;
		padding: 10px;
		font-size: 16px;
		outline: none;
	}
</style>
