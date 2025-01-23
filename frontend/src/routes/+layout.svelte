<script lang="ts">
	import Menu from '~icons/lucide/menu'
	import Sun from '~icons/lucide/sun'
	import Moon from '~icons/lucide/moon'
	import '../app.css';
	import { on } from 'svelte/events';
	import { onMount } from 'svelte';
	import { page } from '$app/state';  
	  
	let {children } = $props();
	// let { data } = $props();
	let draw = $state(false)

	

	onMount(() => {
		if (page.route.id === "/") {
			toggle()
		} else {
			draw = true
		}
	})

	async function toggle() {
		await new Promise( resolve => setTimeout(resolve, 200))
		draw = !draw
	}

</script>

<div>
	{#if draw}
		<div class="navbar w-full flex justify-between h-16 border-t border-b fixed top-0 bg-base-100 z-30">
			<div class="w-full flex justify-evenly">
				<details class="dropdown absolute left-0 ml-4">
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
				<h1 class="text-2xl font-bold"><a href="/">Robert Geraghty</a></h1>
				<div class="absolute right-4">
					<label class="flex cursor-pointer gap-2">
						<Sun/>
						<input type="checkbox" value="black" class="toggle theme-controller" />
						<Moon/>
					  </label>
				</div>	
				  
				<!-- <input type="checkbox" value="black" class="toggle theme-controller absolute right-0 mr-4" /> -->
			</div>
		</div>
	{/if}
	

{@render children()}

<div class="footer footer-center p-10 border-t">
	<div class="grid grid-cols-2 md:flex text-2xl">
		<a href="/" class="btn btn-ghost normal-case text-2xl">Home</a>
		<a href="/projects" class="btn btn-ghost normal-case text-2xl">Projects</a>
		<a href="/blog" class="btn btn-ghost normal-case text-2xl">Blog</a>
		<a href="/contact" class="btn btn-ghost normal-case text-2xl">Contact</a>
	</div>
	<div>
		<p>Copyright © 2025 - All right reserved</p>
	</div>
</div>

</div>

