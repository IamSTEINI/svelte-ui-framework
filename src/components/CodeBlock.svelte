<script lang="ts">
	import Icon from '@iconify/svelte';
	import loader from '@monaco-editor/loader';
	import { onMount, onDestroy } from 'svelte';

	type Code = {
		file: string;
		code: string;
	};

	export let codeblock: Code;

	let editor: any = null;
	let monaco: any = null;
	let editorContainer: HTMLElement;
	let editorLoaded = false;
	let copyStatus = '';

	const LINE_HEIGHT = 20;
	const MAX_HEIGHT = 500;

	function inferLanguage(filename: string) {
		const ext = filename?.split('.')?.pop()?.toLowerCase();
		switch (ext) {
			case 'css':
				return 'css';
			case 'svelte':
				return 'html';
			default:
				return 'plaintext';
		}
	}

	onMount(async () => {
		try {
			monaco = await loader.init();
			const lang = inferLanguage(codeblock?.file ?? '');
			editor = monaco.editor.create(editorContainer, {
				value: codeblock?.code ?? '',
				language: lang,
				readOnly: true,
				minimap: { enabled: false },
				automaticLayout: true,
				scrollBeyondLastLine: false,
				theme: 'vs-dark'
			});

			updateEditorHeight();
			editorLoaded = true;
		} catch (e) {
			console.error('Monaco failed', e);
			editorLoaded = false;
		}
	});

	onDestroy(() => {
		if (editor) {
			editor.dispose();
			editor = null;
		}
	});

	$: if (editor && codeblock) {
		const val = codeblock.code ?? '';
		if (editor.getValue() !== val) editor.setValue(val);
		const model = editor.getModel();
		const lang = inferLanguage(codeblock.file);
		if (model && monaco) {
			monaco.editor.setModelLanguage(model, lang);
		}

		updateEditorHeight();
	}

	function updateEditorHeight() {
		try {
			const text = codeblock?.code ?? '';
			const lines = text == '' ? 1 : text.split('\n').length;
			const height = Math.min(MAX_HEIGHT, Math.max(40, lines * LINE_HEIGHT));
			if (editorContainer && typeof editorContainer.style.setProperty == 'function') {
				editorContainer.style.setProperty('--editor-height', `${height}px`);
			}
			if (editor && typeof editor.layout == 'function') {
				editor.layout();
			}
		} catch (e) {}
	}

	async function copy() {
		try {
			await navigator.clipboard.writeText(codeblock.code ?? '');
			copyStatus = 'Copied!';
			setTimeout(() => (copyStatus = ''), 1200);
		} catch (e) {
			copyStatus = 'Failed';
			setTimeout(() => (copyStatus = ''), 1200);
		}
	}
</script>

<section>
	<div class="titlebar">
		<span>{codeblock.file}</span>
		<button on:click={copy} aria-label="Copy code">
			<Icon style="color: #fff3e9;" icon="material-symbols:content-copy-rounded" />
			{#if copyStatus}{copyStatus}{:else}Copy{/if}
		</button>
	</div>

	<div class="editor" bind:this={editorContainer}>
		{#if !editorLoaded}
			<div class="loaderwrapper">
				<Icon
					style="font-size: 20px;color:#fff3e9;margin-right: 5px;"
					icon="svg-spinners:90-ring" />
				<span>Loading</span>
			</div>
		{/if}
	</div>
</section>

<style>
	section {
		background-color: #232329;
		border-radius: 5px;
		border: 1px #454551 solid;
		word-wrap: break-word;
		width: 99%;
	}

	.titlebar {
		display: flex;
		flex-direction: row;
		border-bottom: 1px #454551 solid;
		padding: 10px;
		align-items: center;
		justify-content: space-between;
		width: 97%;
	}

	.loaderwrapper {
		@apply w-full h-full flex flex-row items-center justify-center;
	}

	.editor {
		width: 100%;
		height: var(--editor-height, auto);
		overflow: hidden;
		max-height: 500px;
	}

	.editor {
		background: transparent;
	}

	:global(.monaco-editor),
	:global(.monaco-editor .overflow-guard),
	:global(.monaco-editor .margin),
	:global(.monaco-editor .monaco-editor-background),
	:global(.monaco-editor .view-lines),
	:global(.monaco-editor .view-line),
	:global(.monaco-editor .lines-content),
	:global(.monaco-editor .inputarea),
	:global(.monaco-scrollable-element) {
		--vscode-editor-background: transparent !important;
		--vscode-editorStickyScroll-border: transparent !important;
		--vscode-editorStickyScroll-shadow: transparent !important;
		--vscode-editorStickyScroll-background: #454551;
		--vscode-editorStickyScrollGutter-background: #454551;
		scrollbar-width: none !important;
		-ms-overflow-style: none !important;
		background-color: transparent !important;
		background: transparent !important;
	}
</style>
