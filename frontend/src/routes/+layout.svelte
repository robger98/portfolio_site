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
	// let theme_controller: HTMLInputElement | undefined = $state()
	// let theme = $state()
	let openDropdown: boolean = $state(false)
  
	function handleClickItem() {
		// close it
		openDropdown = false
	}

	async function handleOnFocusOut() {
		await new Promise( resolve => setTimeout(resolve, 100))
		openDropdown = false
	}



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

<div class="min-h-dvh">
	{#if draw}
		<div class="navbar w-full flex min-h-16 ax-h-16 h-16 justify-between shadow-sm bg-base-100 border-t border-b border-base-300 fixed top-0 z-30">
			<div class="w-full flex justify-between align-middle">
				<details class="group dropdown ml-2" bind:open={openDropdown} onfocusout={handleOnFocusOut}>
					<summary class="btn btn-ghost p-0">
						<Menu class="text-xl"/>
					</summary>
					<ul class="menu border absolute top-[64px] m-0 p-0 shadow bg-base-100 w-52">
						<li><a href="/" onclick={handleClickItem}>Home</a></li>
						<li><a href="/projects" onclick={handleClickItem}>Projects</a></li>
						<li><a href="/blog" onclick={handleClickItem}>Blog</a></li>
						<li><a href="/contact" onclick={handleClickItem}>Contact</a></li>
					</ul>
				</details>
				<h1 class="text-xl font-bold"><a href="/">Robert Geraghty</a></h1>
				<div class="flex mr-2">
					<label class="swap swap-rotate self-center">
						<!-- this hidden checkbox controls the state -->
						<input type="checkbox" class="theme-controller hidden" value="black" />
						<!-- sun icon -->
						<Sun class="swap-on fill-current text-xl"/>
						<!-- moon icon -->
						<Moon class="swap-off fill-current text-xl"/>
					</label	>
				</div>	
				  
				<!-- <input type="checkbox" value="black" class="toggle theme-controller absolute right-0 mr-4" /> -->
			</div>
		</div>
	{/if}
	
{@render children()}

{#if !(page.url.pathname === '/projects/ai-chat')}
	<div class="footer footer-center p-10 border-t border-base-300">
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

	
{/if}
</div>

