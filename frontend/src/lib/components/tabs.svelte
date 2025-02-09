<script lang="ts">
	import { onMount } from "svelte";

    let { items, activeTabValue = $bindable('')}: { items: string[], activeTabValue: string }= $props();
    let count = $derived(items.length)
    let percentage = $derived((count / 100) * 100)
    
    onMount(() => {
        if (!activeTabValue && items.length > 0){
            activeTabValue = items[0];
        }
    });
</script>

<!-- {@render children()} -->
<ul class="w-full">
  {#each items as item}
      <li class={(activeTabValue === item ? 'active text-white ' : 'text-base-content') + ' w-full md:w-fit md:rounded-t-xl'} style={(activeTabValue === item ? 'background-color:#262626' : '')}>
        <button class="border border-b-0 w-full md:w-fit md:rounded-t-xl" onclick={()=>{activeTabValue = item}}>
          <span class=''>{item}</span>
        </button>
      </li>
  {/each}
</ul>
<style>

ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
    border-bottom: 1px solid #dee2e6;
}
li {
	margin-bottom: -1px;
}

span {
    border: 1px solid transparent;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    display: block;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

li.active > button {
    border: none;
}
</style>
