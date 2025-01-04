from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    description="An agent that searches the web using DuckDuckGo.",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the resource in the response"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    description="An agent that provides financial information.",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            company_info=True,
            company_news=True,
            analyst_recommendations=True,
        )
    ],
    instructions=[
        "Use tables to display the results.",
        "Always include the resource in the response",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)


app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
