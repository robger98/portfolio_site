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
				<details class="dropdown absolute left-0">
					<summary class="btn btn-ghost">
						<Menu class="" style="font-size: xx-large;"/>
					</summary>
					<ul class="menu absolute left-0 top-16 p-2 shadow bg-base-100 rounded-box w-52">
						<li><a href="/">Home</a></li>
						<li><a href="/projects">Projects</a></li>
						<li><a href="/blog">Blog</a></li>
						<li><a href="/contact">Contact</a></li>
					</ul>
				</details>
				<!-- <button class="btn btn-ghost absolute left-0">
					<Menu class="" style="font-size: xx-large;"/>
				</button> -->
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

<div class="footer footer-center p-10 bg-base-300 text-base-content">
	<div>
		<p>Copyright © 2023 - All right reserved</p>
	</div>
</div>

</div>

