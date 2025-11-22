<script>
	import Icon from '@iconify/svelte';
</script>

<footer>
	<div
		style="padding-left: 25px;padding-right:25px;"
		class="flex flex-col">
		<h1>SVELTE UI FRAMEWORK</h1>
		<div class="footer-foot">
			<p class="w-fit">My first framework with SVELTE, for SVELTE.</p>
			<a href="https://github.com/IamSTEINI" style="align-items: center;display:flex;">
				<Icon icon="mdi:github" style="font-size: x-large;" />
				IamSTEINI
			</a>
		</div>
	</div>
</footer>

<style>
	footer {
        z-index: 100;
		bottom: 0;
		left: 0;
		width: 100%;
		border-top: 1px #454551 solid;
		background-color: #232329;
	}
	.footer-foot {
		display: flex;
		transform: translateY(-10px);
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
	}
</style>
