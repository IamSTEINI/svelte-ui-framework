<script>
	import { page } from '$app/stores';
	import CodeBlock from '../../../components/CodeBlock.svelte';
	import { onMount } from 'svelte';
	$: name = ($page.params.name ?? '').replace(/^./, (c) => c.toUpperCase());

	/** @type {any} */
	let codeblocks = {};
	let cssCode = '';
	let svelteCode = '';

	onMount(async () => {
		try {
			const res = await fetch('/codeblocks.json');
			if (res.ok) {
				codeblocks = await res.json();
			}
		} catch (e) {
			console.error('Failed to load codeblocks json', e);
		}
	});

	$: if (codeblocks && name) {
		const key = name.toLowerCase();
		const entry = codeblocks[key] ?? {};
		cssCode = entry['11'] ?? '';
		svelteCode = entry['12'] ?? '';
	}
</script>

<svelte:head>
	<title>{name} - Component</title>
</svelte:head>

<section class="codewrapper">
	<h1>{name}</h1>
	{#if name.toLowerCase() == 'button'}
		<h2>CSS</h2>
		<CodeBlock codeblock={{ file: 'style.css', code: cssCode }} />
		<h2>Svelte</h2>
		<CodeBlock codeblock={{ file: 'Button.svelte', code: svelteCode }} />
	{:else if name.toLowerCase() == 'link'}
		<h2>CSS</h2>
		<CodeBlock codeblock={{ file: 'style.css', code: cssCode }} />
		<h2>Svelte</h2>
		<CodeBlock codeblock={{ file: 'Link.svelte', code: svelteCode }} />
	{/if}
</section>

<style>
	section {
		width: 100%;
		max-width: 800px;
		display: flex;
		flex-direction: column;
		align-items: start;
	}
	.codewrapper {
		height: 100%;
		overflow-y: scroll;
		-ms-overflow-style: none;
		scrollbar-width: none;
	}

	:global(.codewrapper)::-webkit-scrollbar {
		display: none;
	}
</style>
