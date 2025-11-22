<script lang="ts">
	import Icon from '@iconify/svelte';
</script>

<header>
	<h1 style="font-size: larger;">THE SVELTE UI FRAMEWORK</h1>
	<button>
		Get started
		<Icon style="font-size: large;" icon="material-symbols:keyboard-double-arrow-right-rounded" />
	</button>
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
</style>
