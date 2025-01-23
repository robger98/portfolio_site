<script lang="ts">

let { children } = $props();

</script>

<div class="h-16"></div>

<div class="flex flex-col items-center">
    {@render children()}
</div>
