<script lang="ts">
  import Post from '$lib/notebooks/maa-analysis.svelte'
  import Prism from 'prismjs';
  import { onMount } from 'svelte';
  
  let holder : HTMLDivElement | undefined = $state()
</script>



<div class="flex justify-center md-container w-full max-w-[1280px]" bind:this={holder}>
  <Post width={holder?.clientWidth} height=600/>    
</div>  

<svelte:head>
  <link href="/prism-vsc-dark-plus.css" rel="stylesheet" />
</svelte:head>