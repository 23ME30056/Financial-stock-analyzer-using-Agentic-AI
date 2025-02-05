from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import openai
web_agent = Agent(
    name="web agent",
    role="search the web for information",
    #  model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    #  model=Groq(id="llama-3.1-70b-versatile"),
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI agent",
    #  model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
     model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["use tables"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),

    instructions=["Always include sources", "use tables"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recommendation and  share the latest news for Nvidia",stream = True)
