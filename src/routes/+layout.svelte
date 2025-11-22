<script lang="ts">
	import Footer from './Footer.svelte';
	import Header from './Header.svelte';
	import './layout.css';
	
	let { children } = $props();
</script>

<div class="app">
	<Header />

	<main>
		{@render children()}
	</main>

	<Footer />
</div>