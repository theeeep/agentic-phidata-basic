from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


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
    instructions="Use tables to display the results. Always include the resource in the response",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

finance_agent.print_response("Summarize analyst recomendations for NVDA", stream=True)
