<script lang="ts">
    // TODO: In severe need of commenting
    // TODO: In severe need of refactoring
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
    import Tabs from "$lib/components/tabs.svelte";
    import TabPanel from "$lib/components/tabPanel.svelte";
    import { CreateTreeFromGitElement } from "$lib/components/tree.svelte";
	import { on } from "svelte/events";
	import { scale } from "svelte/transition";

    let { data }= $props();

    let repoName: string = $state('portfolio_site');
    let repoInput: string | undefined = $state();

    let accountName: string = $state('robger98');
    let accountInput: string | undefined = $state();

    let branchesReady = $state(false);

    let branches: string[] = $state(['master']);
    let repoBranch: string = $state('master');

    let selectedFile: GitElement | undefined = $state();
    let fileElement: GitFile | undefined = $state();

    let repotree: GitElement | undefined = $state();

    let flattened_tree: GitElement[] | undefined = $derived(repotree? flattenTree(repotree) : undefined);

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
        repo_view_svg;
    });

    $effect(() => {
        repo_view_svg;
        pie_svg;
    });

    $effect(() => {
        width = viz_container?.clientWidth || 400;
        height = viz_container?.clientHeight || 400;
    });
    
    let pie_chart_container: HTMLDivElement | undefined = $state();
    let pie_chart_width = $state(400);
    let pie_chart_height = $state(400);


    let pie_chart_file_count_data = $derived.by(() => {
        if (!repotree) return [];
        const flattened_tree = flattenTree(d3_working_root.data)
        if (!flattened_tree) return [];
        const langCount = new Map();
        for (const el of flattened_tree) {
            if (el.is_dir) continue;
            
            const lang = el.language || 'Unknown';
            langCount.set(lang, (langCount.get(lang) || 0) + 1);
        }
        return Array.from(langCount, ([name, value]) => ({ name, value }));
    });

    let pie_chart_file_size_data = $derived.by(()=>{
        if (!repotree) return [];
        const flattened_tree = flattenTree(d3_working_root.data )
        if (!flattened_tree) return [];
        const langCount = new Map();
        for (const el of flattened_tree) {
            if (el.is_dir) continue;
            const lang = el.language || 'Unknown';
            langCount.set(lang, (langCount.get(lang) || 0) + el.size );
        }
        return Array.from(langCount, ([name, value]) => ({ name, value }));
    })


    let activeDisplayTab: string = $state('File Distibution by Type');
    let show_count = $derived(activeDisplayTab === 'File Distibution by Type')

   

    let viz_container: HTMLDivElement | undefined = $state();
    let width = $state(400);
    let height = $state(400);
    
    let margin = $state({top: 20, right: 20, bottom: 30, left: 40});
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
        const out = (maxDim) / (nodeSize * 2.1);
        return out;
    }

    let packed = $derived.by(() => {
        const layout = d3.pack<GitElement>();   
        layout.size([width, height]).radius(((node) => Math.sqrt(node.data.size || 1)));
        return layout(d3_working_root);
    });

    let repo_view_svg = $derived.by(() => {
        if (viz_container) {
            viz_container.innerHTML = '';
        } else {
            return
        }
        
        const pack = d3.select(viz_container)
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .style('background-color', '#262626')
            .style('radius', '')
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

    let pie_svg = $derived.by(() => {
        if (pie_chart_container) {
            pie_chart_container.innerHTML = '';
        } else {
            return
        }

        const pie = d3.pie<{name: string, value: number}>()
            .value(d => show_count? d.value : (d.value))
            .sort((a, b) => d3.ascending(a.value, b.value));
        
        const arc = d3.arc<d3.PieArcDatum<{name: string, value: number}>>()
            .innerRadius(Math.min(pie_chart_width, pie_chart_height) / 10)
            .outerRadius(Math.min(pie_chart_width, pie_chart_height) / 2.5)
            .padAngle(0.025);
        
        

        const svg = d3.select(pie_chart_container)
            .append('svg')
            .attr('width', pie_chart_width)
            .attr('height', pie_chart_height)
            .style('background-color', '#262626')
            .on('zoom', function(event, d) {
                const {transform} = event;
                console.log(event)
            })
            .append('g')
            .attr('transform', `translate(${pie_chart_width / 2}, ${pie_chart_height / 2})`);
        
        const data = show_count ? pie_chart_file_count_data : pie_chart_file_size_data;
        const color = d3.scaleOrdinal()
            .domain(data.map(d => d.name))
            .range(d3.schemeTableau10);
            
        const pie_data = pie(data);

        const label_positions2 = (() => {
            let top_left = pie_data.filter(d => (d.startAngle + d.endAngle)/2 >= Math.PI*1.5);
            top_left.sort((a, b) => d3.ascending(a.startAngle, b.startAngle));
            let bottom_left = pie_data.filter(d => (d.startAngle + d.endAngle)/2 >= Math.PI*1 && (d.startAngle + d.endAngle)/2 < Math.PI*1.5);
            bottom_left.sort((a, b) => d3.descending(a.startAngle, b.startAngle));
            let bottom_right = pie_data.filter(d => (d.startAngle + d.endAngle)/2 >= Math.PI*0.5 && (d.startAngle + d.endAngle)/2 < Math.PI*1);
            bottom_right.sort((a, b) => d3.ascending(a.startAngle, b.startAngle));
            let top_right = pie_data.filter(d => (d.startAngle + d.endAngle)/2 < Math.PI*0.5);
            top_right.sort((a, b) => d3.descending(a.startAngle, b.startAngle));

            const threshold = 35;
            const padding = 10;
            const x_padding = 10;
            let d_y = new Map()
            let last_y = 0;
            for (let i = 0; i < top_left.length; i++) {
                const d = top_left[i];
                const angle = (d.startAngle + d.endAngle) / 2;
                let y = Math.sin(angle-Math.PI/2) * (arc.outerRadius()(d) + padding);
                let x = (-pie_chart_width/2)+x_padding;
                const diff = Math.abs(y - last_y);
                if ( !(y < last_y && diff > threshold) && i!=0) {
                    y = last_y-(threshold);
                }
                d_y.set(top_left[i].data.name, [x,y]);
                last_y = y;
            }

            for (let i = 0; i < bottom_left.length; i++) {
                const d = bottom_left[i];
                const angle = (d.startAngle + d.endAngle) / 2;
                let y = Math.sin(angle-Math.PI/2) * (arc.outerRadius()(d) + padding);
                const x = (-pie_chart_width/2)+x_padding;
                const diff = Math.abs(y - last_y);
                if (!(y > last_y && diff > threshold) && i!=0) {
                   y = last_y+(threshold);
                }
                d_y.set(bottom_left[i].data.name, [x,y]);
                last_y = y;
            }

            for (let i = 0; i < bottom_right.length; i++) {
                const d = bottom_right[i];
                const angle = (d.startAngle + d.endAngle) / 2;
                let y = Math.sin(angle-Math.PI/2) * (arc.outerRadius()(d) + padding);
                const x = (pie_chart_width/2)-x_padding;
                const diff = Math.abs(y - last_y);
                if (!(y > last_y && diff > threshold) && i!=0) {
                     y = last_y+(threshold);
                }
                d_y.set(bottom_right[i].data.name, [x, y]);
                last_y = y;
            }

            for (let i = 0; i < top_right.length; i++) {
                const d = top_right[i];
                const angle = (d.startAngle + d.endAngle) / 2;
                let y = Math.sin(angle-Math.PI/2) * (arc.outerRadius()(d) + padding);
                const x = (pie_chart_width/2)-x_padding;
                const diff = Math.abs(y - last_y);
                if (!(y < last_y && diff > threshold) && i!=0) {
                    y = last_y-(threshold);
                    
                }
                d_y.set(top_right[i].data.name, [x,y]);
                last_y = y;
            }

            return d_y;
        })();

        const text_anchors = (() => {
            let left_d = pie_data.filter(d => (d.startAngle + d.endAngle)/2 > Math.PI)
            let right_d = pie_data.filter(d => (d.startAngle + d.endAngle)/2 < Math.PI)

            let num_left = left_d.length;
            let num_right = right_d.length;

            let d_anchor = new Map()
            for (let i = 0; i < num_left; i++) {
                d_anchor.set(left_d[i].data.name, 'start');
            }
            
            for (let i = 0; i < num_right; i++) {
                d_anchor.set(right_d[i].data.name, 'end');
            }
            return d_anchor;
        })();

        svg.selectAll('slices')
            .data(pie_data)
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', d => color(d.data.name))
            // .attr('stroke', 'white')
            // .attr('stroke-width', '2px')
            .style('opacity', 1)
            .on('mouseover', function(event, d) {
                d3.select(this).style('opacity', 0.5);
                svg.selectAll('text').filter(t => t === d)
                    .style('fill', 'grey');
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            })
            .on('mouseout', function(event, d) {
                d3.select(this).style('opacity', 1);
                svg.selectAll('text').filter(t => t === d)
                    .style('fill', 'white');
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'blue');
            })
            .on('click', function(event, d) {
                repo_view_svg?.selectAll('circle')
                    .filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            });

        function place_labels_on_edge_of_pie_window(d : d3.PieArcDatum<{name: string, value: number}>) {
            
        }

        function position_labels_outside_slice(d: d3.PieArcDatum<{name: string, value: number}>) {
            const angle = (d.startAngle + d.endAngle) / 2;
            const x = Math.cos(angle-Math.PI/2) * (arc.outerRadius()(d) + 20);
            const y = Math.sin(angle-Math.PI/2) * (arc.outerRadius()(d) + 20);
            return `translate(${x}, ${y})`;
        }

        

        svg.selectAll('polyline')
            .data(pie_data)
            .enter()
            .append('polyline')
            .attr('points', function(d) {
                const angle = (d.startAngle + d.endAngle) / 2;
                const y = label_positions2.get(d.data.name)[1];
                const pad = (y/Math.sin(angle-Math.PI/2))-arc.outerRadius()(d) 
                const centroid = arc.centroid(d);
                let x = Math.cos(angle-Math.PI/2) * (arc.outerRadius()(d) + pad);
                const label_x = label_positions2.get(d.data.name)[0];
                

                return [centroid, x ,y , label_x, y];
            })
            .attr('stroke', d => color(d.data.name))
            .attr('stroke-width', '2px')
            .style('fill', 'none')
            .style('opacity', 1)
            .on('mouseover', function(event, d) {
                svg.selectAll('path').filter(t => t === d)
                    .style('opacity', 0.5);
                svg.selectAll('text').filter(t => t === d)
                    .style('fill', 'grey');
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            })
            .on('mouseout', function(event, d) {
                svg.selectAll('path').filter(t => t === d)
                    .style('opacity', 1);
                svg.selectAll('text').filter(t => t === d)
                    .style('fill', 'white');
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'blue');
            })
            .on('click', function(event, d) {
                repo_view_svg?.selectAll('circle')
                    .filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            });
        
        svg.selectAll('slices')
            .data(pie_data)
            .enter()
            .append('text')
            .text(function(d){ return "." + d.data.name + ": " + (show_count? d.data.value : convertBytesToHumanReadable(d.data.value))})
            .attr('x', d=> label_positions2.get(d.data.name)[0] || 0)
            .attr('y', d=> label_positions2.get(d.data.name)[1]-10 || 0)
            .attr('class', 'pie-label')
            .style("text-anchor", d => text_anchors.get(d.data.name))
            .style("font-size", 20)
            .style('fill', 'white')
            .style('opacity', 1)
            .on('mouseover', function(event, d) {
                d3.select(this).style('fill', 'gray');
                svg.selectAll('path').filter(t => t === d)
                    .style('opacity', 0.5);
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            })
            .on('mouseout', function(event, d) {
                d3.select(this).style('fill', 'white');
                svg.selectAll('path').filter(t => t === d)
                    .style('opacity', 1);
                repo_view_svg?.selectAll('circle').filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'blue');
            })
            .on('click', function(event, d) {
                repo_view_svg?.selectAll('circle')
                    .filter(t => t.data.language === d.data.name && !t.data.is_dir)
                    .style('fill', 'red');
            });


        const zoom = d3.zoom<SVGSVGElement, unknown>().scaleExtent([0, Infinity]).on('zoom', zoomed)
        svg.call(zoom);

        function zoomed(event) {
            const {transform} = event;
            svg.selectAll('path').attr('transform', transform);
            svg.selectAll('polyline').attr('transform', transform);
            svg.selectAll('text').attr('transform', transform);
        }
        const padded_height = pie_chart_height - 20
        const radius = Math.min(pie_chart_width, pie_chart_height) / 2.5
        const max_y = Math.max(Math.max(...Array.from(label_positions2.values()).map(d => d[1])), radius);
        const min_y = Math.min(...Array.from(label_positions2.values()).map(d => d[1]), -radius);
        const center_y = (max_y + min_y)/2;
        let scale_factor = 1;
        if (padded_height < Math.abs(min_y - max_y)) {
            scale_factor = padded_height/(Math.abs(min_y - max_y)+40);
            
        }

        zoom.transform(svg, d3.zoomIdentity.translate(0, -center_y*scale_factor).scale(scale_factor));
       

        
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

    function getLargestFile(): GitElement | undefined {
        if (repotree) {
            const files = d3_root.descendants().filter((node) => !node.data.is_dir);
            if (files.length > 0) {
                return files.reduce((largest, file) => {
                    return (file.data.size || 0) > (largest.data.size || 0) ? file : largest;
                }).data;
            }
        }
        return undefined;
    }

    function convertBytesToHumanReadable(bytes: number): string {
        const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
        if (bytes === 0) return '0 Bytes';
        const i = Math.floor(Math.log(bytes) / Math.log(1024));
        return Math.round((bytes / Math.pow(1024, i))*100)/100 + ' ' + sizes[i];
    }


    let current_request = $state();

    async function get_file(selected: GitElement) {
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
        repo_view_svg;  
    }

    onMount(async () => {
        width = viz_container?.clientWidth || 400;
        height = viz_container?.clientHeight || 400;
        await update_data();
        repo_view_svg;
        if (file_view_selection && file_view) {
            ;
        }
        
    })

</script>

<div id="page" class="w-full md:h-[calc(100dvh-64px)] md:max-h-[calc(100dvh-64px)] bg-base-300 flex flex-col">
    <div class="top-bar bg-base-100 text-base-content p-2 w-full flex justify-between items-center place-content-center pl-4 pr-4">
        <div id="repo-branch-selection" class="flex flex-col md:flex-row items-center md-container gap-4">
            <h2 class="md:hidden text-center">This dashboard is designed with desktops in mind</h2>
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
            <div class="card-body flex flex-col max-h-full p-2 gap-0">
                <div class="card-title">Repo Summary</div>
                <div class="divider w-full m-0"></div>
                <div class="flex flex-col grow gap-1 bg-base-300 rounded-xl p-2 pl-4 pr-4 overflow-auto">
                    <div class="flex w-full justify-between gap-2">
                        <div class="">File count</div> 
                        <div>{flattened_tree?.filter(x => !x.is_dir).length || 0}</div>
                    </div>
                    <div class='divider w-full m-0'></div>
                    <div class="flex w-full justify-between gap-2">
                        <div class="">Total Size</div> <div>{convertBytesToHumanReadable(repotree?.size || 0)}</div>
                    </div>
                    <div class='divider w-full m-0'></div>
                    <div class="flex w-full justify-between gap-2">
                        <div class="">Average File Size</div> <div>{convertBytesToHumanReadable(computeAverageSize())}</div>
                    </div>
                    <div class='divider w-full m-0'></div>
                    <div class='flex w-full justify-between gap-2' >
                        <div class="">Median File Size</div> <div>{convertBytesToHumanReadable(computeMedianSize())}</div>
                    </div>
                    <div class='divider w-full m-0'></div>
                    <div class="flex w-full justify-between gap-2">
                        <div class="">Largest File Size</div> <div>{convertBytesToHumanReadable(getLargestFile()?.size || 0)}</div>
                    </div>
                </div>
            </div>
            
        </div> 
        <div id="file-list" class="nd:col-span-1 md:row-start-1 md:row-span-4 card border border-base-300 bg-base-100 rounded-2xl shadow p-4 flex flex-col">
            <div class="flex flex-col grow max-h-full">
                <div class="card-title">File List</div>
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
        <div id="repo-viz" class="min-h-96 grow md:grow-0 md:min-h-0 md:max-h-full md:col-start-2 md:row-start-1 md:col-span-3 md:row-span-3 card border bg-base-100 border-base-300 rounded-2xl shadow">
            <div class="card-body flex flex-col max-h-full p-4">
                <div>
                    <div class='card-title'>Repo Visualization</div>
                    <div class="pb-2"> Click on the nodes to dive in, click outside the nodes to return to parent.</div>
                </div>
                <div class='flex grow min-h-96 md:min-h-0 w-full bg-base-300 max-h-full rounded-b-xl overflow-clip' bind:this={viz_container} bind:clientHeight={height} bind:clientWidth={width}>
                </div>
            </div>
        </div>
        <div id="histogram" class="md:col-start-2 md:row-start-4 md:col-span-3 row-span-3 card border border-base-300 bg-base-100 rounded-2xl shadow p-4">
            <div class='card-body flex flex-col max-h-full p-2 gap-0'>
                <div class='card-title'>File type summaries</div>
                <div class="pb-2">Hover on a file type in a chart to highlight it in the repo visualization. </div>
                <div>
                    <Tabs 
                    bind:activeTabValue={activeDisplayTab}
                    items={['File Distibution by Type', 'File Size Distibution by Type']}/>
                </div>
                <div class="flex grow min-h-96 md:min-h-0 w-full bg-base-300 max-h-full rounded-b-xl overflow-clip" bind:clientWidth={pie_chart_width} bind:clientHeight={pie_chart_height} bind:this={pie_chart_container}>
                </div>
                <div class="text-xs text-gray-500 pt-2">(Note: label placement is <a href="https://en.wikipedia.org/wiki/Automatic_label_placement" class='text-blue-500'>hard</a>. I took a pretty simple approach but it might be a bit unruly on smaller screens)</div>
            </div>
            
        <div class='pie-label'></div>
            
        </div>
        <div id="file_preview" class="md:col-span-2 md:row-span-6 card border border-base-300 bg-base-100 rounded-2xl shadow p-4 max-w-full max-h-full">
            <div class="card-body flex flex-col max-h-full p-2">
                <div class="card-title">File View</div>
                <div class="divider w-full m-0"></div>
                <div class="grow max-h-full overflow-hidden">
                    {#if fileElement}
                        <FileInfo file={fileElement}/>
                    {:else}
                        <p>Click on a file to view the source code.</p>
                    {/if}
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    h1 {
        font-size: 1.5rem;
    }
</style>