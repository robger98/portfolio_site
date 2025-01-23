## AI Chat Interface

This is a simple AI chat interface that I used to familiarize myself with Sveltekit and FastAPI.
<br/><br/>

#### Model
This chat utilizes OpenAI's gpt4o-mini.
<br/><br/>

#### Backend
SvelteKit + FastAPI
<br/><br/>
For messsage handling, I am using Python with FastAPI. The API is simple, with only a single POST route for
sending messages to the backend. The entire chat history is sent 
in the request message since this example is running without any 
database for storing different chat histories or chat sessions.
<br/><br/>
In Python, the message is processed, prompts are applied, and the full message is sent to OpenAI using langchain.
<br/><br/>

#### Frontend
Svelte + TailwindCSS + DaisyUI
<br/><br/>
#### Extensions
While this example is fairly simple, I have used this general format in other projects with further capabilities.
Some examples include:
- RAG agents
- Multi-agent chat systems
- Multi-session applications
- Multi-user applications
  
I plan to add some more feature-rich examples to this portfolio soon! 