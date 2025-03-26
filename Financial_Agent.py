from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

financial_agent = Agent(
    name = "Financial Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,company_info=True,stock_fundamentals=True,analyst_recommendations=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."]
)

financial_agent.print_response("Summarize and compare analyst recommendations and fundamentals for TESLA vs NVIDIA stocks.")