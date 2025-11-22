<script lang="ts">
	import Icon from '@iconify/svelte';
</script>

<header>
	<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<h1 on:click={() => (window.location.href = '/')} style="font-size: larger;cursor: pointer;">
		THE SVELTE UI FRAMEWORK
	</h1>
	<div class="row">
		<a href="/about">What's this?</a>
		<button>
			Get started
			<Icon style="font-size: large;" icon="material-symbols:keyboard-double-arrow-right-rounded" />
		</button>
	</div>
</header>

<style>
	header {
		@apply justify-between items-center flex flex-row;
		top: 0;
		left: 0;
		width: 95%;
		max-width: 800px;
		height: 50px;
		padding-left: 10px;
		padding-right: 10px;
		background-color: #232329;
		border-radius: 5px;
		border: 1px #454551 solid;
	}
	.row {
		display: flex;
		flex-direction: row;
		align-items: center;
		gap: 10px;
	}
</style>
