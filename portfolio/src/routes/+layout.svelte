<script lang="ts">
	import Menu from '~icons/lucide/menu'
	import '../app.css';
	import { on } from 'svelte/events';
	import { onMount } from 'svelte';
	let { children } = $props();
	let draw = $state(false)

	let theme = $state()
	let themelist = [
			"business",
			"black", 
			"light", 
			"dark", 
			"cupcake", 
			"forest", 
			"halloween", 
			"lofi", 
			"pastel", 
			"wireframe", 
			"synthwave", 
			"retro", 
			"cyberpunk", 
			"valentine", 
			"dracula", 
			"aqua", 
			"black", 
			"luxury", 
			"night", 
			"soda", 
			"emerald", 
			"corporate"
		]
	theme = "black"
	onMount(() => {
		toggle()
	})

	async function toggle() {
		await new Promise( resolve => setTimeout(resolve, 200))
		draw = !draw
	}

</script>

<div data-theme="{theme}">
	{#if draw}
		<div class="navbar w-full flex justify-between h-16 border-t border-b fixed bg-inherit z-30">
			<div class="w-full flex justify-evenly">
				<button class="btn btn-ghost absolute left-0">
					<Menu class="" style="font-size: xx-large;"/>
				</button>
				<a class="text-xl md:text-4xl font-altehaas text-center" href="/">Robert Geraghty</a>
			</div>
			<!-- <div class="dropdown">
				<div class="">
					<span class="hidden md:inline mr-1">Theme</span>
					<select class="select select-bordered" bind:value={theme}>
						{#each themelist as t}
							<option value={t}>{t}</option>
						{/each}
					</select>
				</div>
			</div> -->
		</div>
	{/if}

{@render children()}

</div>

