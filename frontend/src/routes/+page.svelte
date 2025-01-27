<script>
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

<div class="relative h-screen w-full grid grid-cols-1">
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
    <div class="h-24"></div>
    <div class="p-4 flex flex-col items-center main-content">
        <img src={"/headshot.jfif"} width="560" height="560" alt="Robert Geraghty" class="rounded-full w-32 h-32 md:w-64 md:h-64 mb-3" style="object-fit: cover;"/>
        <h1 class="font-bold text-2xl font-altehaas text-center mb-2">Hello!</h1>
        <p class="text-justify">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Cras a sodales eros. Aliquam malesuada eget sem in feugiat. Fusce 
            malesuada egestas leo, et volutpat velit fermentum eget. Class 
            aptent taciti sociosqu ad litora torquent per conubia nostra, per 
            inceptos himenaeos. Sed sollicitudin rhoncus ultrices. Cras mattis 
            sagittis est at volutpat.
        </p>
        <div class="divider"></div>
        <div class="card shadow-lg rounded-lg border">
            <h2 class="card-title pl-2 pt-2"> Skills</h2>
            <ul class="card-body list-disc text-justify">
                <li>Maecenas tristique felis eget aliquet sodales.</li>
                <li>Maecenas ut felis egestas, hendrerit nisi id, sodales nulla.</li>
                <li>Vivamus nec dolor vitae libero lacinia sollicitudin a et ex.</li>
                <li>Mauris scelerisque metus a fermentum vestibulum.</li>
                <li>Mauris et risus porta, egestas risus non, laoreet libero.</li>
                <li>Donec nec diam porttitor risus posuere faucibus id in nisl.</li>
            </ul>
            
        </div>
        <!-- <div class="h-screen w-full"></div> -->
        <!-- <span class="text-center"></span> -->
    </div>
</div>

