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

    let { data }= $props();

    let repoName: string = $state('portfolio_site');
    let repoInput: string | undefined = $state();

    let accountName: string = $state('robger98');
    let accountInput: string | undefined = $state();

    let branchesReady = $state(false);

    let branches: string[] = $state(['main']);
    let repoBranch: string = $state('main');

    let selectedNode: d3.HierarchyCircularNode<GitElement> | undefined = $state();
    let selectedFile: GitElement | undefined = $state();
    let fileElement: GitFile | undefined = $state();

    let repotree: GitElement | undefined = $state();
    let flattened_tree: GitElement[] | undefined = $state();
    let viz_container: HTMLDivElement | undefined = $state();
    let width = $derived((viz_container?.clientWidth || 400));
    let height = $derived((viz_container?.clientHeight || 400));
    
    let margin = $state({top: 20, right: 20, bottom: 30, left: 40});
    let svg: d3.Selection<SVGSVGElement, unknown, null, undefined> | undefined= $state();
    let d3_root: d3.HierarchyNode<GitElement> | undefined = $state();
    let d3_working_root: d3.HierarchyNode<GitElement> | undefined = $state();

    let zoom = d3.zoom<SVGSVGElement, unknown>().on('zoom', handleZoom);
    let showLog = $state(false);

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

    function handleZoom(event: any) {
        const {transform} = event;
        svg?.selectAll('circle').attr('transform', transform);
        svg?.selectAll('text').attr('transform', transform);
        svg?.selectAll('.link1').style("stroke-width", 8/transform.k);
    }

    async function get_file() {
        const response = await getFile({
            client: client,
            path: {
                account: accountName,
                repo_name: repoName,
                branch: repoBranch,
                path: selectedFile?.full_path || ''
            }
        });
        if (response?.data) {
            
            fileElement = response.data;
        } else {
            console.error('Error getting file:', response);
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

    function on_pack_click(event: MouseEvent, d: d3.HierarchyCircularNode<GitElement>) {
        if (event && event.stopPropagation) {
            event.stopPropagation();
        }
        selectedNode = d;
        d3_working_root = d3.hierarchy(selectedNode.data)
        if (!d.data.is_dir) {
            selectedFile = d.data;
            get_file();
        }
        update_graphic()
    }

    function on_svg_click() {
        const parent_name = d3_working_root?.data.parent_name || '';
        if (d3_root) {
            d3_working_root = d3.hierarchy(findElementByName(parent_name) || d3_root.data);
            
        }
        update_graphic();
    }

    function update_graphic() {
        if (viz_container) {
            viz_container.innerHTML = '';
        }
        if (d3_working_root && viz_container) {
            const packLayout = d3.pack<GitElement>()
            if (d3_working_root.data.size) {
                packLayout.size([width, height]).padding(3).radius(((node)=> Math.log2(node.data.size||1)));
            }
            // d3_root.sum(() => 1);
            const packed = packLayout(d3_working_root);

            svg = d3.select(viz_container)
                .append('svg')
                .attr('width', width)
                .attr('height', height)
                .on('click', on_svg_click);

            svg.selectAll('circle')
                .data(packed.descendants())
                .enter()
                .append('circle')
                .attr('cx', d => d.x)
                .attr('cy', d => d.y)
                .attr('r', d => d.r || 5)
                .style('opacity', 0.3)
                .style('fill', 'blue')
                .style('stroke', 'white')
                .style('stroke-width', d => d.r/100)
                .on('click', on_pack_click)
                .on('mouseover', function(event, d) {
                    d3.select(this).style('fill', 'red');
                    svg.selectAll('text').filter(t => t === d)
                        .style('opacity', 1);
                })
                .on('mouseout', function(event, d) {
                    d3.select(this).style('fill', 'blue');
                    svg.selectAll('text').filter(t => t === d)
                        .style('opacity', 0);
                })

            svg.selectAll('text')
                .data(packed.descendants())
                .enter()
                .append('text')
                .attr('x', d => d.x)
                .attr('y', d => d.y)
                .attr('text-anchor', 'middle')
                .attr('dy', '0.3em')
                .text(d => d.data.name || "/")
                .style('font-size', d => Math.max(12, (2*d.r)/(d.data.name||'/').length) + 'px')
                .style('fill', 'White')
                .style('opacity', 0)
                .style('pointer-events', 'none');


            svg.call(zoom);
        }
    }

    async function update_data() {
        repoName = repoInput?.trim() || repoName;
        accountName = accountInput?.trim() || accountName;
        if (viz_container) {
            viz_container.innerHTML = 'Loading...';
        }
        await get_repo();
        // {console.log(repotree)}
        if (repotree) {
            d3_root = d3.hierarchy(repotree);
            d3_working_root = d3_root;
        }

        update_graphic();       
    }

    onMount(async () => {
       update_data();
    })
</script>

<div id="page" class="w-full h-[calc(100dvh-64px)] max-h-[calc(100dvh-64px)] bg-base-300 flex flex-col">
    <div class="top-bar bg-base-100 text-base-content p-2 w-full flex justify-between items-center pl-4 pr-4">
        <div id="repo-branch-selection" class="flex items-center gap-4">
            <p>Enter public github repo information here:</p>
            <div id="repo-info" class="flex items-center">
                
                <input type="text" id="account" bind:value={accountInput} onkeydown={disableReady} placeholder="Account Name" class="input input-sm border-none input-primary grow bg-base-300"/>
                <div class="divider divider-horizontal">/</div>
                    <input type="text" id="repo" bind:value={repoInput} onkeydown={disableReady} placeholder="Repo Name" class="input input-sm border-none input-primary grow bg-base-300"/>
                <button class="ml-4" onclick={async ()=> await get_branches()}><Search class=""/></button>
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

    <div class="grid grid-cols-6 grid-rows-6 w-full grow gap-4 p-4 ">
        <div id="descriptive-stats" class="col-span-1 row-span-2 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class="flex flex-col">
                <p>Average File Size: {computeAverageSize()} bytes</p>
                <p>Median File Size: {computeMedianSize()} bytes</p>
                <p>Largest File</p>
                <p>Smallest File</p>
                <p>Largest Directory</p>
                <p>Smallest Directory</p>
            </div>
        </div> 
        <div id="file-list" class="col-span-1 row-start-3 row-span-4 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class="flex flex-col">
                <p>File List</p>
            </div>
        </div>
        <div id="histogram" class="col-start-2 row-start-1 col-span-3 row-span-2 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class="flex flex-col place-items-center md-container">
                <h1>This is currently WIP</h1>
            </div>
        </div>
        <div id="repo-viz" class="col-start-2 row-start-3 col-span-3 row-span-4 card border bg-base-100 border-base-300 rounded-2xl shadow ">
            <div class="card-body">
                <div class='card-title'>Repo Visualisation</div>
                <div> Click on the nodes to dive in, click outside the nodes to return to parent.</div>
                <div class='grow bg-base-300 rounded-xl' bind:this={viz_container}>
                </div>
                
            </div>
        </div>
        <div id="file_preview" class="col-span-2 row-span-6 card border border-base-300 bg-base-100 rounded-2xl shadow p-4 max-w-full">
            {#if fileElement}
                <FileInfo file={fileElement}/>
            {:else}
                <p>No file selected</p>
            {/if}
        </div>
    </div>
</div>
