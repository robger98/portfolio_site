<script lang="ts">
    import { getMessagesMessagesGet, sendSendPost, client } from "$lib/client/sdk.gen";
    import type { Message } from "$lib/client/types.gen";
    import MessageCard from "$lib/components/messageCard.svelte";
    import Markdown from '@magidoc/plugin-svelte-marked'
    import AboutMD from './about.md?raw';
	import { onMount } from "svelte";

    let inputMessage = $state('');
    let messages: Message[] = $state<Message[]>([])
    let element: HTMLDivElement | null = null;
    let drawertoggle: HTMLInputElement | null = null;
    client.setConfig({baseUrl:'http://localhost:8000'});

    async function handleSubmit(event: KeyboardEvent) {
        // if ((Date.now() - lastMessageTime) < 500) {
        //     return;
        // }
        // lastMessageTime = Date.now();
        console.log(event);
        if (event.key === 'Enter' && !event.shiftKey && inputMessage.trim()) {
            console.log('Sending message:', inputMessage);
            const newMessage: Message = {
                role: 'user',
                content: inputMessage
            };
            messages = [...messages, newMessage]
            await new Promise(resolve => setTimeout(resolve, 20)); // Force re-render
            inputMessage = ''; // Clear input after sending
            try {
                const response = await sendSendPost({
                    client: client,
                    body: messages
                });
                if (response?.data) {
                    messages = [...messages, response.data];
                } else {
                    messages = [...messages, {role: 'System', content: 'No model response'}];
                }
            } catch (error) {
                console.error('Error sending message:', error);
            }
        }
    }
    
    $effect(() => {const m = messages; scrollToBottom(element);})

    const scrollToBottom = async (node: any) => {
        if (!node) return;
        // node.lastElementChild?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
    }; 

    onMount((async () => {
        await new Promise(resolve => setTimeout(resolve, 200));
        drawertoggle?.click();
    }));

</script>




<div class="drawer">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" bind:this={drawertoggle}/>
    <div class="h-[calc(100lvh-80px)] flex flex-col drawer-content place-items-center mb-4 mr-4 ml-4">
        <label for="my-drawer-2" class="btn btn-ghost">About</label>
        <div class="w-full flex flex-col justify-between main-content grow">
            <div class="card h-full border w-full overflow-auto mb-4 p-2" bind:this={element}>
                {#each messages as message}
                    <MessageCard role={message.role} content={message.content}/>
                {/each}
            </div>
            <div class="card w-full border">
                <textarea class='autogrow-textarea textarea' placeholder="Type here..." bind:value={inputMessage} onkeydown={handleSubmit}></textarea>
            </div>
        </div>
    </div>
    <div class="drawer-side">
        <div class="max-w-[80%] lg:max-w-[614px] bg-base-200 absolute min-h-[calc(100lvh-64px)] top-[64px] p-2 flex flex-col">
            <div class="md-container"><Markdown source={AboutMD}/></div>
            <br/>
            
            <label for="my-drawer-2" aria-label="close sidebar" class="btn bg-base-300 justify-self-center">Get Chatting!</label>
        </div>
        <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay bg-transparent -z-10"></label>
    </div>
    </div>
