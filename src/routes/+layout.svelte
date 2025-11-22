<script lang="ts">
	import Footer from './Footer.svelte';
	import Header from './Header.svelte';
	import './layout.css';
	
	let { children } = $props();
</script>

<div class="app w-screen h-screen">
	<Header />

	<main class="display-childs">
		{@render children()}
	</main>

	<Footer />
</div>

<style>
	.app {
		overflow-x: hidden;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 15px;
	}
	.display-childs {
		height: 95vh;
	}
</style>