from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name = "Financial Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,company_info=True,stock_fundamentals=True,analyst_recommendations=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."]
)

agent_team = Agent(
    team=[web_agent,financial_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=['Always include sources',"use tables to display data."],
    show_tool_calls = True,
    markdown = True
)

agent_team.print_response("Summarize and compare analyst recommendations and fundamentals for TESLA vs NVIDIA stocks.",streams=True )