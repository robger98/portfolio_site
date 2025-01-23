<script lang="ts">


    let { data } = $props();
    let grid_def = $state();

</script>

<div class="flex flex-col main-content md:grid items-center md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
    {#each data.projects as {name, description, link}}
    {console.log(data.projects.length)}
        <div class="card col-span-1 w-full h-96 border shadow-xl">
            <div class="card-body">
                <h1 class="card-title">{name}</h1>
                <p>{description}</p>
                <a href={link} class="btn btn-primary">View Project</a>
            </div>
        </div>
    {/each}
</div>