from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

# This is just an LLM wrapped inside an Agent, nothing Agentic here.
web_agent = Agent(

    model=Groq(id="llama-3.3-70b-versatile")
   
)
web_agent.print_response("Tell me about OpenAI Sora?", stream=True)