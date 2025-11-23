<script>
	import Icon from '@iconify/svelte';
</script>

<section>
	<div class="inputwrapper">
		<input type="text" placeholder="Input with icon" />
		<Icon style="color: white;opacity: 0.5;" icon="material-symbols:search-rounded" />
	</div>
</section>

<style>
	.inputwrapper {
		display: flex;
		flex-direction: row;
		align-items: center;
		padding: 10px;
		background-color: #232329;
		border-radius: 5px;
		border: 1px #454551 solid;
	}

	.inputwrapper input {
		outline: none;
		border: none;
		background-color: transparent;
		color: white;
		font-size: 12px;
	}
</style>
