

<script lang="ts">
    import { onMount } from "svelte";

    let { activeValue = $bindable(), classes, value, children } = $props();

    onMount(() => {
        console.log(children, "mounted");
    });
</script>

<div class={(activeValue === value ? 'block' : 'hidden') + ' ' + classes}>
    {@render children?.()}
</div>
