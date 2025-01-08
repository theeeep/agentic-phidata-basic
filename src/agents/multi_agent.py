from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from web_search_agent import web_search_agent
from finance_agent import finance_agent

load_dotenv()


agent_team = Agent(
    name="Agent Team",
    description="A team of agents working together to perform tasks.",
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=[
        "Always include resources in the response.",
        "Use Tables to display the results.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)
agent_team.print_response(
    "Summarize analyst recomendations and share the latest news for Apple", stream=True
)
