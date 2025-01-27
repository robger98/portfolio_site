#### Background

My first exposure to web development was early in high school. I was part of my high school's [iGEM](https://igem.org/) team, and part of the competition involved having a website. 
Being the computer nerd I was (and am) I led the development of our website. 
At the age of 14 armed with a "html for dummies" book and zero experience, I went on to try and make our website.
<br/><br/>
Now while I was able to get a website up and running, it was far from the prettiest thing the world has ever seen. 
I boldly attempted to create my own responsive CSS grid-based framework (which worked*) and grew frustrated with what at the time seemed needlessly finicky. 
With a life-long passion for art I could see perfectly how I wanted things to look and two div's being one pixel off was not a part of that vision.
<br/><br/>
For better or worse this experience left a pretty sour taste in my mouth for web-development, a taste that I carried throughout much of my time as a CS student and computer nerd. 
I gravitated towards headless software, not wanting or needing to hack through the weeds of front-end development, 
but that is not to say I completely disregarded how my UI's looked. 
I frequented [ASCII art generator sites](https://patorjk.com/software/taag/#p=display&f=Delta%20Corps%20Priest%201&t=Robert's%20Rad%20Software) to give my CLI (command line interface) applications fun splash screens (see Fig. 1) and looked to other ASCII based projects for inspiration to turn simple CLI's into TUI's (terminal user interface).
<div class="flex flex-col items-center p-4">
    <img src="/RobertsRadSoftware.PNG" alt="Rad ASCII Art" width="500">
    <p class="text-center">Fig. 1: Very cool ASCII art</p>
</div>

#### Moving forward
Despite the bad taste of high school webdev, there comes a time when the attraction of a GUI overpowers the distaste for its means. 
Wanting to take the path of least resistance, and with fondness and experience in Python, I decided to explore the world of python frontend development. 
I first started playing around with [Streamlit](https://streamlit.io/), finding its simplicity to very attractive. 
I still think it is a great tool for quickly getting data powered applications into the hands of stakeholders and users but with the simplicity came limitations.
While I'm sure I could try to beat it into submission to conform to my vision I figured it would be better to move on to something more complex but with fewer guardrails. 
<br/><br/>
I did some digging and learned about [NiceGUI](https://nicegui.io/), which seemed to provide a nice balance between simplicity, performance, and customizability. 
I developed a couple of tools/webapps with it for practice, and found it to be pretty great for most of my use-cases. 
It is still my go-to if I am developing a native application in Python today. 
However, and much like my past experiences, I still felt like I had to hack in some features when the behavior I was looking for was not directly supported. NiceGUI does provide a way to run javascript in python, but when I found my code littered with too many instances of `ui.run_javascript('way too much JS for a python program...')` I figured it was time to bite the bullet and return to "real" web development.
<br/><br/>

#### So Many Choices
To say I was confused returning to standard web dev frameworks is an understatement. 
Of course, I had heard of some of the big names before, React, Angular, Bootstrap, etc. but I had very little knowledge of what they were and what they were used for. When I start something, I like to start with a plan and I like to invest my time in something I won't just drop weeks later, so I performed the standard [Google searches](https://letmegooglethat.com/?q=Best+way+to+make+website+work+good%3F%3F%3F) one does when they are trying to learn a new skill.
After much reddit reading, project restarting, `npm` confusioning, and [tier list](https://2024.stateofjs.com/en-US/libraries/#tier_list) viewing, I settled on [Svelte](https://svelte.dev/).
<br/><br/>

#### Svelte
Svelte, more so than other frameworks I reviewed, seems to make things easy.
It's not perfect, and I'm still very much learning, but it (in combination with other frameworks, such as [TailwindCSS](https://tailwindcss.com/)) feels intuitive in a way I hadn't experienced before with web/gui development. 
Features like runes for state variables and updating components with data changes auto-magically just made sense to me and allowed me to learn rapidly. 
The only downside I have seen so far is the relatively small community around it when compared to giants like React.
Admittedly, there is less of a job market for Svelte at the moment, but I'm not trying to be a web developer, so this is not a huge drawback.
It can make learning by example hard, but the framework is straight-forward enough and my questions common enough that I have been able to find answer with low to moderate digging.  
<br/><br/>

#### Other Considerations
While this website might not be anything to write home about, it represents a huge growth in my skills, and on top of the nuts and bolts of the website itself, it gave me an excuse to deepen my understanding of several skills, including:
- **HTML/CSS**: Sure these are the basics, but I have had somewhat limited exposure to these tools and practice is practice
- **Docker**: For containerizing the frontend and backend for deployment
- **Google Cloud Run**: For hosting the containers
- **Cybersecurity Practices****: For not exposing API keys and other potentially dangerous information to the world at large.
- **API Development**: Communicating with the [FastAPI](https://fastapi.tiangolo.com/) backend for the [AI Chat](/projects/ai-chat) 
<br/><br/>

#### Moving forward (pt. 2)
Now that I have the bones of a website here, I plan to revamp and add work both old and new to better showcase my skills and log my personal growth as a data scientist/developer/computer nerd (well really, a general nerd). Depending on when you are reading this, this showcase may look somewhat sparse. All that that means is I'm working on it.
<br/><br/>
<div class="text-center text-2xl text-bold">
Thank you for reading, and I hope you enjoy the site 😁
</div>


<br/><br/><br/>
*for the most part
<br/>
**I am not a cybersecurity professional, this item is not a challenge, **please don't hack me!**