<script lang="ts">
	import { onMount } from "svelte";

    let { items, activeTabValue = $bindable('')}: { items: string[], activeTabValue: string }= $props();
    
    onMount(() => {
        if (!activeTabValue && items.length > 0){
            activeTabValue = items[0];
        }
    });
</script>

<!-- {@render children()} -->
<ul>
  {#each items as item}
      <li class={activeTabValue === item ? 'active' : ''}>
        <button class="border border-b-0" onclick={()=>{activeTabValue = item}}>
          <span>{item}</span>
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
    color: #495057;
    background-color: #fff;
    border-color: #dee2e6 #dee2e6 #fff;
}
</style>
