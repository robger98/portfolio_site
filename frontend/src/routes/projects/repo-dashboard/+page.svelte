<script lang="ts">
    // import client from "$lib/client/sdk.gen";
    import { 
        client, 
        getBranchesRepoAccountRepoNameBranchesGet as getBranches,
        getRepoRepoAccountRepoNameBranchGet as getRepo,
        getFileRepoAccountRepoNameBranchPathGet as getFile
    } from "$lib/client/sdk.gen";
    import FileInfo from "$lib/components/fileInfo.svelte";
    import type { 
        GitElement, 
        GitFile,
    } from "$lib/client/types.gen";
    

    import Search from "~icons/lucide/search"
    import ArrowUp from "~icons/lucide/arrow-up"
	import { onMount } from "svelte";
    import * as d3 from 'd3';
	import { get } from "svelte/store";
	import Tree from "$lib/components/tree.svelte";
    import type { TreeItem } from "$lib/components/tree.svelte";
    import { CreateTreeFromGitElement } from "$lib/components/tree.svelte";
	import { on } from "svelte/events";
	// import { TEMP } from "$env/static/private";

    let { data }= $props();

    let repoName: string = $state('portfolio_site');
    let repoInput: string | undefined = $state();

    let accountName: string = $state('robger98');
    let accountInput: string | undefined = $state();

    let branchesReady = $state(false);

    let branches: string[] = $state(['main']);
    let repoBranch: string = $state('main');

    let selectedFile: GitElement | undefined = $state();
    let fileElement: GitFile | undefined = $state();

    // let fileInfo: FileInfo | undefined = $state();

    // $inspect('selectedFile', selectedFile, 'fileElement', fileElement);

    let repotree: GitElement | undefined = $state();

    let flattened_tree: GitElement[] | undefined = $state();

    let displayTree: TreeItem | undefined = $derived(repotree? CreateTreeFromGitElement(repotree) : undefined);
    let file_view: Tree | undefined = $state();
    let file_view_selection: TreeItem | undefined = $state();
    let last_file_view_selection: TreeItem | undefined = $state();

    $effect(() => {
        if (file_view_selection !== last_file_view_selection) {
                last_file_view_selection = file_view_selection;
                if (!last_file_view_selection) {
                    last_file_view_selection = file_view_selection;
                }
                if (file_view_selection) {
                    selectedFile = findElementByName(file_view_selection.name);
                    (async () => {
                        if (selectedFile) {
                            fileElement = await get_file(selectedFile);   
                        }
                    })();
                }
        } else {
            (async () => {
                if (selectedFile) {
                    fileElement = await get_file(selectedFile);   
                }
            })();
        }
    });

    $effect(() => {
        if (file_view_selection && selectedFile) {
            
        }
        svg;
    });

    $effect(() => {
        svg;
    });

    $effect(() => {
        width = viz_container?.clientWidth || 400;
        height = viz_container?.clientHeight || 400;
    });
    
    let viz_container: HTMLDivElement | undefined = $state();
    let width = $state(400);
    let height = $state(400);
    
    let margin = $state({top: 20, right: 20, bottom: 30, left: 40});
    // let svg: d3.Selection<SVGSVGElement, unknown, null, undefined> | undefined= $state();
    let d3_root: d3.HierarchyNode<GitElement> = $derived(
        repotree? d3.hierarchy<GitElement>(repotree) : d3.hierarchy<GitElement>({name: 'root', is_dir: true, children: [], size: 0, full_path: ''})
    );


    let d3_working_root: d3.HierarchyNode<GitElement> = $derived.by(() => {
        if (selectedFile) {
            return d3.hierarchy<GitElement>(selectedFile); 
        } else {
            return d3_root;
        }
    });

    function computeFitScale(nodeSize: number, width: number, height: number): number {
        const maxDim = Math.min(width, height);
        // For a node with radius = nodeSize, we ensure the diameter fits
        const out = (maxDim) / (nodeSize * 2.1);
        return out;
    }

    let packed = $derived.by(() => {
        const layout = d3.pack<GitElement>();   
        layout.size([width, height]).radius(((node) => Math.sqrt(node.data.size || 1)));
        return layout(d3_working_root);
    });

    let svg = $derived.by(() => {
        if (viz_container) {
            viz_container.innerHTML = '';
        } else {
            return
        }
        
        const pack = d3.select(viz_container)
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .on('click', function(event, d) {
                const parent_name = d3_working_root?.data.parent_name || '';
                selectedFile = findElementByName(parent_name);
            });
        
       

        pack.selectAll('circle')
            .data(packed.descendants())
            .enter()
            .append('circle')
            .attr('id', d => d.data.full_path)
            .attr('cx', d => d.x)
            .attr('cy', d => d.y)
            .attr('r', d => d.r || 5)
            .style('opacity', 0.3)
            .style('fill', 'blue')
            .style('stroke', 'white')
            .style('stroke-width', d => d.r/100)
            .style('stroke-opacity', 1)
            .on('click', function(event, d) {
                if (event && event.stopPropagation) {
                    event.stopPropagation();
                }
                if (!d.data.is_dir) {
                    selectedFile = d.data;
                } else {
                    selectedFile = d.data;
                }
            })
            .on('mouseover', function(event, d) {
                d3.select(this).style('fill', 'red');
                pack?.selectAll('text').filter(t => t === d)
                    .style('opacity', 1);
            })
            .on('mouseout', function(event, d) {
                d3.select(this).style('fill', 'blue');
                pack?.selectAll('text').filter(t => t === d)
                    .style('opacity', d.parent === packed ? 1 : d===packed && !d.data.is_dir? 1 : 0);
            })

        pack.selectAll('text')
            .data(packed.descendants())
            .enter()
            .append('text')
            .attr('x', d => d.x)
            .attr('y', d => d.y)
            .attr('text-anchor', 'middle')
            .attr('dy', '0.3em')
            .text(d => d.data.name || "/")
            .style('font-size', d =>  (2*d.r)/(d.data.name||'/').length + 'px')
            .style('fill', 'White')
            .style('opacity', d => d.parent === packed ? 1 : d===packed && !d.data.is_dir? 1 : 0)
            .style('pointer-events', 'none');
        
        d3.select(window).on('resize.updatesvg', ()=>{
            pack.attr('width', width).attr('height', height);
        });

        const scale = computeFitScale(packed.r, width, height);

        const zoom = d3.zoom<SVGSVGElement, unknown>().scaleExtent([scale, Infinity]).on('zoom', zoomed)
        pack.call(zoom);

        function zoomed(event) {
            const {transform} = event;
            pack.selectAll('circle').attr('transform', transform);
            pack.selectAll('text').attr('transform', transform);
            pack.selectAll('.link1').style("stroke-width", 8/transform.k);
        }
        
        
    
        zoom.scaleBy(pack, scale);

        return pack;
    });

    client.setConfig({baseUrl:data.API_URL});
    
    function computeAverageSize() {
        if (d3_root) {
            const total_size = d3_root.data.size || 1;
            const total_nodes = d3_root.descendants().length;
            return Math.round(total_size/total_nodes);
        }
        return 1;
    }
    
    function computeMedianSize() {
        if (d3_root) {
            const sizes = d3_root.descendants().map((node) => node.data.size || 1);
            sizes.sort();
            const mid = Math.floor(sizes.length/2);
            if (sizes.length % 2 === 0) {
                return (sizes[mid-1] + sizes[mid])/2;
            } else {
                return sizes[mid];
            }
        }
        return 1;
    }

    let current_request = $state();

    async function get_file(selected: GitElement) {
        console.log('Getting file:', selected);
        console.log('Current request:', current_request);
        if (selected.is_dir) {
            return undefined;
        }
        if (fileElement?.path === selected.full_path) {
            return fileElement;
        } else {
            if (current_request === selected.full_path) {
                return undefined;
            }
            current_request = selected.full_path;
            const response = await getFile({
                client: client,
                path: {
                    account: accountName,
                    repo_name: repoName,
                    branch: repoBranch,
                    path: selected.full_path || ''
                }
            });
            current_request = '';
            if (response?.data) {
                return response.data;
            } else {
                return undefined;
                console.error('Error getting file:', response);
            }
            
        }
    }

    async function get_branches() {
        accountName = accountInput?.trim() || accountName;
        repoName = repoInput?.trim() || repoName;
        const response = await getBranches({
            client: client,
            path: {account: accountName, repo_name: repoName}
        });
        if (response?.data) {
            
            branches = response.data;
            repoBranch = branches[0];
            branchesReady = true;
        } else {
            console.error('Error getting branches:', response);
        }
    }

    function findElementByName(name: string): GitElement | undefined {
        var found = undefined;
        flattened_tree?.forEach((git_element) => {
            
            if (git_element.name === name) {
                
                found = git_element;
            }
        });
        return found;
    }

    function flattenTree(root: GitElement): GitElement[] {
        const result: GitElement[] = [];
        function traverse(node: GitElement) {
            result.push(node);
            if (node.children) {
                node.children.forEach((child) => traverse(child));
            }
        }
        traverse(root);
        return result;
    }   

    async function get_repo() {
        const response = await getRepo({
            client: client,
            path: {
                account: accountName,
                repo_name: repoName,
                branch: repoBranch
            }
        });
        if (response?.data) {
            repotree = response.data;
            flattened_tree = flattenTree(repotree);
        } else {
            console.error('Error getting repo:', response);
        }
    }

    function disableReady() {
        
        branchesReady = false;
    }


    async function update_data() {
        repoName = repoInput?.trim() || repoName;
        accountName = accountInput?.trim() || accountName;
        if (viz_container) {
            viz_container.innerHTML = 'Loading...';
        }
        await get_repo();
        selectedFile = repotree;
        fileElement = undefined;
        file_view_selection = undefined;
        svg;  
    }

    onMount(async () => {
        width = viz_container?.clientWidth || 400;
        height = viz_container?.clientHeight || 400;
        await update_data();
        svg;
        if (file_view_selection && file_view) {
            ;
        }
        
    })
</script>

<div id="page" class="w-full md:h-[calc(100dvh-64px)] md:max-h-[calc(100dvh-64px)] bg-base-300 flex flex-col">
    <div class="top-bar bg-base-100 text-base-content p-2 w-full flex justify-between items-center place-content-center pl-4 pr-4">
        <div id="repo-branch-selection" class="flex flex-col md:flex-row items-center md-container gap-4">
            <h2 class="md:hidden text-center">Please note this dashboard is designed with desktops in mind</h2>
            <p>Enter public github repo information here:</p>
            <div id="repo-info" class="flex flex-col md:flex-row items-center justify-center max-w-full">
                <div class="flex flex-col sm:flex-row items-center w-full sm:w-fit">
                    <input type="text" id="account" bind:value={accountInput} onkeydown={disableReady} placeholder="Account Name" class="input input-sm border-none input-primary grow bg-base-300 w-full sm:w-fit"/>
                    <div class="hidden md:block divider divider-horizontal w-full sm:w-fit">/</div>
                    <div class="md:hidden divider divider-vertical w-full sm:w-fit m-0"></div>
                    <input type="text" id="repo" bind:value={repoInput} onkeydown={disableReady} placeholder="Repo Name" class="input input-sm border-none input-primary grow bg-base-300 w-full sm:w-fit"/>
                </div>
                <button id="searh-repo" class="my-4 md:my-0 md:mx-4 hover:bg-base-200 p-[6px] border rounded" onclick={async ()=> await get_branches()}><Search class=""/></button>
            </div>
            {#if branchesReady}
                <div id="repo-info" class=" flex items-center gap-4">
                    <p>Select Branch</p>
                        <!-- <p>Branch</p> -->
                    <select id="branch" bind:value={repoBranch} class="select select-bordered place-content-center select-sm max-w-xs text-xs" disabled={!branchesReady}>
                        {#each branches as branch}
                            <option value={branch}>{branch}</option>
                        {/each}
                    </select>
                </div>
                <button class="btn btn-primary" onclick={update_data} disabled={!branchesReady}>Update</button>
            {/if}
        </div>
    </div>  

    <div class="flex flex-col md:grid md:grid-cols-6 md:grid-rows-6 w-full grow gap-4 p-4 md:max-h-[calc(100dvh-136px)]">
        <div id="descriptive-stats" class="md:col-span-1 md:row-span-2 md:row-start-5 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class="flex flex-col">
                <p>Average File Size: {computeAverageSize()} bytes</p>
                <p>Median File Size: {computeMedianSize()} bytes</p>
                <p>Largest File</p>
                <p>Smallest File</p>
                <p>Largest Directory</p>
                <p>Smallest Directory</p>
            </div>
        </div> 
        <div id="file-list" class="nd:col-span-1 md:row-start-1 md:row-span-4 card border border-base-300 bg-base-100 rounded-2xl shadow p-4 flex flex-col">
            <div class="flex flex-col grow max-h-full">
                <h1>File List</h1>
                <div class="divider w-full m-0"></div>
                {#if displayTree}
                {#key displayTree}
                    <Tree tree={displayTree} classes="overflow-auto max-h-full bg-base-300 p-2 rounded-xl grow" bind:this={file_view} bind:selection={file_view_selection}>

                    </Tree>
                {/key}
                {:else}
                    <p>Loading...</p>
                {/if}
            </div>
        </div>
        <div id="histogram" class="md:col-start-2 md:row-start-5 md:col-span-3 row-span-2 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class="flex flex-col place-items-center md-container">
                <h2>Full functionality currently under construction</h2>
            </div>
        </div>
        <div id="repo-viz" class="min-h-96 grow md:grow-0 md:min-h-0 md:max-h-full md:col-start-2 md:row-start-1 md:col-span-3 md:row-span-4 card border bg-base-100 border-base-300 rounded-2xl shadow">
            <div class="card-body flex flex-col max-h-full p-4">
                <div>
                    <div class='card-title'>Repo Visualisation</div>
                    <div class="truncate text-ellipsis"> Click on the nodes to dive in, click outside the nodes to return to parent.</div>
                </div>
                <div class='h-full max-h-[calc(100%-52px)] bg-base-300 rounded-xl' bind:this={viz_container} bind:clientHeight={height} bind:clientWidth={width}>
                    <!-- <svg class='w-full h-full max-h-full' ></svg> -->
                </div>
            </div>
        </div>
        <div id="file_preview" class="md:col-span-2 md:row-span-6 card border border-base-300 bg-base-100 rounded-2xl shadow p-4 max-w-full max-h-full">
            {#if fileElement}
                <FileInfo file={fileElement}/>
            {:else}
                <p>No file selected.  </p>
            {/if}
        </div>
    </div>
</div>

<style>
    h1 {
        font-size: 1.5rem;
    }
</style>