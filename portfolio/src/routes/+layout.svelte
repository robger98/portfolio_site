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
		<div class="navbar w-full flex justify-between h-16 border-t border-b fixed top-0 bg-inherit z-30">
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
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="20"
						  height="20"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round">
						  <circle cx="12" cy="12" r="5" />
						  <path
							d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4" />
						</svg>
						<input type="checkbox" value="black" class="toggle theme-controller" />
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="20"
						  height="20"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round">
						  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
						</svg>
					  </label>
				</div>	
				  
				<!-- <input type="checkbox" value="black" class="toggle theme-controller absolute right-0 mr-4" /> -->
			</div>
		</div>
	{/if}
	

{@render children()}



<div class="footer footer-center p-10 mt-10 border-t">
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

