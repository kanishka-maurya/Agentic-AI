import streamlit as st
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()

# Define Agents
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=False
)

financial_agent = Agent(
    name="Financial Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, company_info=True, stock_fundamentals=True, analyst_recommendations=True)],
    show_tool_calls=False,
    instructions=["Use tables to display data."],
)

# Create Agent Team
agent_team = Agent(
    team=[web_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data."],
    show_tool_calls=False
)

# Streamlit App
st.set_page_config(page_title="Financial & Web AI Agent", layout="wide")
st.title("💹 AI-Powered Financial & Web Agent")
st.write("Ask any financial or web-related question, and our AI agents will provide insights with sources!")

# User Input
query = st.text_area("Enter your query:", placeholder="Summarize and compare analyst recommendations and fundamentals for TESLA vs NVIDIA stocks.")

if st.button("Get Response"):
    with st.spinner("Generating response..."):
        try:
            # For non-streaming response
            response = agent_team.run(query, stream=False)
            
            # Initialize empty container
            response_placeholder = st.empty()
            
            # Extract content based on response type
            if hasattr(response, 'content'):
                full_response = response.content
            else:
                full_response = str(response)
            
            # Display the complete response at once
            response_placeholder.markdown(full_response, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")