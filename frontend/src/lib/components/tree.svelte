<script module lang="ts">
    import type { GitElement } from '$lib/client'
    import { onMount, type Component} from 'svelte'
    import type { SvelteHTMLElements } from 'svelte/elements'

    export type TreeItem = {
        name: string,
        type: string,
        children: TreeItem[]
    }

    export function CreateTreeFromGitElement(GitElement: GitElement): TreeItem {
        let tree: TreeItem = {
            name: GitElement.name? GitElement.name : "",
            type: GitElement.is_dir? '_folder' : 'file',
            children: []
        }
        if (GitElement.children) {
            for (let child of GitElement.children) {
                tree.children.push(CreateTreeFromGitElement(child))
            }
        }
        tree.children.sort((a, b) => a.name.localeCompare(b.name));
        tree.children.sort((a, b) => a.type.localeCompare(b.type));
        return tree
    }

</script>

<script lang="ts">
    import type { TreeItem } from './tree.svelte'
    import Self from './tree.svelte'

    // import { createEventDispatcher } from 'svelte'

    import Folder from '~icons/lucide/folder'
    import FolderOpen from '~icons/lucide/folder-open'
    import File from '~icons/lucide/file'


    let { tree, classes, selection = $bindable() }: {
        tree: TreeItem,
        classes: string,
        selection?: TreeItem
    } = $props();

    let is_clicked: boolean | undefined = $state(false);

    async function handleClick() {
        if (tree.type === 'file') {
            selection = tree;
            return;
        }
        is_clicked = !is_clicked;
    }

    onMount(() => {
        tree.children.sort((a, b) => a.name.localeCompare(b.name));
        tree.children.sort((a, b) => a.type.localeCompare(b.type));
    })
</script>

<div class={'w-full h-fit whitespace-nowrap ' + classes}>
    <ul>
        <li>
            <button class='flex items-center' onclick={handleClick}>
                {#if tree.type === '_folder'}
                    {#if is_clicked}
                        <FolderOpen class=""/>
                    {:else}
                        <Folder class=""/>
                    {/if}
                    <!-- <Folder class=""/> -->
                {:else}
                    <File class=""/>
                {/if}
                <span class='ml-2'>
                {tree.name? tree.name : tree.type === '_folder'? '/' : 'File'}
            </button>
            {#if (tree.children?.length && is_clicked)}
                <ul class='tree-holder'>
                    {#each tree.children as child}
                    <li>
                        <Self tree={child} classes='w-fit h-fit' bind:selection/>
                    </li>
                    {/each}
                </ul>
            {/if}
        </li>
    </ul>
</div>

<style>
    .tree-holder {
        padding-left: 0.75rem;
    }
</style>