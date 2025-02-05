from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.agent import Agent
from agno.models.groq import Groq


agent_storage: str = "tmp/agents.db"
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




app = Playground(agents=[web_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)