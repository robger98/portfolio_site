<script lang="ts">
    import Markdown from '@magidoc/plugin-svelte-marked'
    import 'highlight.js/styles/base16/solarized-dark.css';
    import { CodeBlock } from "svhighlight";
	import { onMount } from "svelte";

    let { role, content } = $props();
    let displayRole = $derived(capitalizeFirstLetter(role))
    // let compiledContent = $state()
    const pattern = /```([\w-]*)[\r|\n|\r\n]?([\s\S]*?)[\r|\n|\r\n]?```/g;

    let splits = $derived(splitContentSegments(content))

    function capitalizeFirstLetter(val: String) {
        return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

    function splitContentSegments(text: string): Array<[boolean, string | undefined, string]> {
        const result: Array<[boolean, string | undefined, string]> = [];
        let lastIndex = 0;
        let match;
        while ((match = pattern.exec(text)) !== null) {
            if (match.index > lastIndex) {
                result.push([false, undefined, text.slice(lastIndex, match.index)]);
            }
            result.push([true, match[1] || undefined, match[2] || '']);
            lastIndex = pattern.lastIndex;
        }
        if (lastIndex < text.length) {
            result.push([false, undefined, text.slice(lastIndex)]);
        }
        return result;
    }
    onMount(async () => {
        // compiledContent = await compile(content)
        // console.log(compiledContent)
    })

</script>
<!-- <p class={(role == 'user'? 'justify-self-end mb-1' : 'justify-self-start mb-1')}>
    {displayRole}
</p> -->
<div class={((role === "user")? " self-end " : " self-start ") + " card bg-base-200 rounded-lg pt-1 pb-1 pr-2 pl-2 max-w-[80%] mb-2 "}>
    {#if role == 'user'}
        <!-- <div class="card border pt-1 pb-1 pr-2 pl-2 max-w-[80%]"> -->
            <p>{content}</p>
        <!-- </div> -->
    {:else}
        <div class="">
            {#each splits as split}
                {console.log(split)}
                {#if split[0]}
                    <CodeBlock
                        language={split[1]}
                        code={split[2]}
                        
                    />     
                    <div class="h-4"></div>
                {:else} 
                    <Markdown source={split[2]}></Markdown>
                {/if}
            {/each}
        </div>
    {/if}
</div>

<!-- <div class={(role == 'user'? 'justify-self-end' : 'justify-self-start') + 'max-w-[75%]'}>
    <p class={(role == 'user'? 'justify-self-end' : 'justify-self-start')}>{role}</p>
    <div class={(role == 'user'? 'bg-slate-200 justify-self-end' : 'justify-self-start') + 'rounded-lg w-fit max-w-full p-4'}>
        {#each splits as split }
            {console.log(split)} -->
            <!-- {#if split[0]} -->
                <!-- <markdo language={split[1]} code={split[2]} lineNumbers></CodeBlock> -->
            <!-- {:else} -->
                <!-- <Markdown source={split[2]}></Markdown> -->
            <!-- {/if} -->
        <!-- {/each} -->
    <!-- </div> -->
<!-- </div> -->
