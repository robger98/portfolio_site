<script lang="ts">
    let { data } = $props();
</script>

<div class="flex flex-col max-w-[1140px] w-full md:grid items-center md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
    {#each data.summaries as {slug, title, date, description}}
        <div class="card col-span-1 w-full h-96 shadow-md border border-base-300">
            <div class="card-body flex flex-col justify-between">
                <div>
                    <h1 class="card-title">{title}</h1>
                    <p>{description}</p>
                </div>
                <div class="flex items-center">
                    <p>{date}</p>
                    <a href="/blog/{slug}" class="btn btn-primary">View Post</a>
                </div>
            </div>
        </div>
    {/each}
</div>

