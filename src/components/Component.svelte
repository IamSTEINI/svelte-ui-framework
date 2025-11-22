<script lang="ts">
	import Icon from '@iconify/svelte';

	type Item = {
		name: string;
		description: string;
		path: string;
		image: string;
	};

	export let item: Item;

	const navigate = () => (location.href = item.path);
</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_noninteractive_element_to_interactive_role -->
<article on:click={navigate} role="link" class="group" tabindex="0">
	<img src={item.image} alt={item.name} width="160" />
	<h1>{item.name}</h1>
	<p class="desc-text">{item.description}</p>
	<span class="hover-text">Click to explore <Icon icon="material-symbols:search-rounded" /></span>
</article>

<style>
	article {
		padding: 15px;
		width: 350px;
        height: 270px;
		background-color: #232329;
		border-radius: 5px;
		border: 1px #454551 solid;
	}
	article:hover {
		cursor: pointer;
		transition: all ease-in 120ms;
		background: linear-gradient(180deg, #2b2b31 0%, #232329 100%);
		border-color: #6b6b75;
	}
	img {
		display: block;
		width: 100%;
		margin-bottom: 0.5rem;
		object-fit: cover;
		border-radius: 5px;
	}

	.desc-text,
	.hover-text {
		display: block;
		transition:
			opacity 160ms ease,
			transform 160ms ease;
		transform-origin: top center;
	}
	.desc-text {
		transform: translateY(0);
		pointer-events: auto;
	}
	.hover-text {
		opacity: 0;
		transform: translateY(6px);
		pointer-events: none;
	}
	article:hover .hover-text,
	article:focus .hover-text {
		opacity: 1;
		transform: translateY(0);
		pointer-events: auto;
		z-index: 2;
	}
	article:hover .desc-text,
	article:focus .desc-text {
		transform: translateY(-6px);
		pointer-events: none;
	}
</style>
