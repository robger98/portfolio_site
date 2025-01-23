<script lang="ts">
    import { getMessagesMessagesGet, sendSendPost, client } from "$lib/client/sdk.gen";
    import type { Message } from "$lib/client/types.gen";
    import MessageCard from "$lib/components/messageCard.svelte";

    let inputMessage = $state('');
    let messages: Message[] = $state<Message[]>([])
    
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
    
</script>



<div class="h-[calc(100lvh-64px)] w-full flex flex-col justify-between main-content">
    <div class="chatarea card h-full border w-full overflow-auto mb-4 mt-4 p-2 grow">
        {#each messages as message}
            <MessageCard role={message.role} content={message.content}/>
        {/each}
    </div>
    <textarea class='autogrow-textarea bg-base-200 mb-4' placeholder="Say Hi!" bind:value={inputMessage} onkeydown={handleSubmit}></textarea>
</div>