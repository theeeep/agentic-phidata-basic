from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    description="An agent that searches the web using DuckDuckGo.",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions="Always include the resource in the response",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

web_search_agent.print_response("Who is Elon Musk?", stream=True)
