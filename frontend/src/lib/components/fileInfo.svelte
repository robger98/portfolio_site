<script lang="ts">
    import type { GitFile } from "$lib/client/types.gen";
    import 'highlight.js/styles/base16/solarized-dark.css';
    import { CodeBlock } from "svhighlight";

    let { file }: {
        file: GitFile,
    } = $props();

    // $inspect('file', file);

    // $effect(() => {
    //     if (file.content !== "Cannot Decode File") {
    //         const element = document.getElementById('file-content');
    //         if (element){
    //             element.innerHTML = '<CodeBlock language=lang code=file.content/>';
    //         }
    //     }
    // })

</script>

<div class="flex flex-col items-center h-full">
    <h1 class="text-2xl font-bold">{file.name}</h1>
    <p class="text-sm text-gray-500">{file.path}</p>
    <p class="text-sm text-gray-500">{file.size}</p>
    <div id="file-content" class="w-full grow max-h-full overflow-auto">
        {#key file.content}
            {#if file.content === "Cannot Decode File"}
                <p>Cannot Decode File</p>
            {:else}
                <CodeBlock language={file.language} code={file.content} dimensions='w-full h-full'/>
            {/if}
        {/key}
    </div>
</div>
