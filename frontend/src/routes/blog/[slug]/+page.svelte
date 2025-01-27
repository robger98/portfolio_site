<script lang="ts">
    import Markdown from "@magidoc/plugin-svelte-marked";
    let { data } = $props();
</script>

<div
  class="hero"
  style="background-image: url({data.post.image});">
  <div class="hero-overlay"></div>
  <div class="hero-content text-white text-center">
    <div class="max-w-md">
      <h1 class="mb-5 text-5xl font-bold">{data.post.title}</h1>
      <p class="">{data.post.description}</p>
    </div>
  </div>
</div>

<div class="p-4 flex flex-col items-center main-content">
    
    <div class="md-container">
        <Markdown source={data.post.content}/>
    </div>
</div>