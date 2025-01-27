<script>
	import Markdown from "@magidoc/plugin-svelte-marked";
    import AboutMe from './about_me.md?raw';
    import Skills from  './skills.md?raw';
    import Technologies from './technologies.md?raw';
    import { onMount } from "svelte";
    import { ThpaceGL } from "thpace";

    import ChevronDown from '~icons/lucide/chevron-down'
    // import headshot from '$lib/assets/headshot.jfif'
    

    onMount(() => {
        const canvas = document.querySelector("#splash");
        if (!(canvas instanceof HTMLCanvasElement)) {
            throw new Error("No canvas element found");
        }
        const settings = {
            colors: ['#000000', '#000000', '#000000'],
            triangleSize: 130,
            particleSettings: {
                count: [.5,2.5],
                interval: [10000, 200000],
                radius: [1, 1],
                opacity: [0, 1  ],
                variationX: 100,
                variationY: 100,
                color: '#ffffff',
            },
        };

        ThpaceGL.create(canvas, settings);
    });

</script>

<div class="relative h-dvh w-full grid grid-cols-1">
    <canvas id="splash" class="absolute top-0 left-0 right-0 bottom-0 z-40"></canvas>
    <div class="p-4  absolute left-0 right-0 self-center justify-self-center flex flex-col items-center z-50 text-white">
        <span class="text-4xl md:text-6xl lg:text-8xl font-bold font-altehaas text-center">Robert Geraghty</span>
        <span class="text-2xl md:text-4xl text-center font-altehaas">Data Scientist</span>
        <div class="h-4 flex">
            <a href="/" class="btn btn-ghost normal-case text-xl font-altehaas">Home</a>
            <a href="/projects" class="btn btn-ghost normal-case text-xl font-altehaas">Projects</a>
            <a href="/blog" class="btn btn-ghost normal-case text-xl font-altehaas">Blog</a>
            <a href="/contact" class="btn btn-ghost normal-case text-xl font-altehaas">Contact</a>
        </div>  
    </div>
    <ChevronDown class="text-6xl absolute bottom-0 mb-0 left-0 right-0 self-center justify-self-center animate-bounce z-50" style="color: white;"/>   
</div>

<div class="flex flex-col items-center">
    <div class="h-16"></div>
    <div class="p-4 flex flex-col items-center main-content">
        <img src={"/headshot.jfif"} width="560" height="560" alt="Robert Geraghty" class="rounded-full w-32 h-32 md:w-64 md:h-64 mb-3" style="object-fit: cover;"/>
        <h1 class="font-bold text-2xl font-altehaas text-center mb-2">Hello!</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 mt-4 gap-4 max-w-full">
            <div class="md-container p-4 md:col-span-2">
                <h2 class="card-title pt-2"> About Me</h2>
                <Markdown source={AboutMe}></Markdown>
            </div>
            <div class="card bg-base-200 shadow-md md-container col-span-1 p-4">
                <h2 class="card-title pt-2"> Skills</h2>
                <Markdown source={Skills}></Markdown>
            </div>
            <div class="card bg-base-200 shadow-md md-container col-span-1 p-4">
                <h2 class="card-title pt-2"> Technologies</h2>
                <Markdown source={Technologies}></Markdown>
            </div>
        </div>  
    </div>
</div>

