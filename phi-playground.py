from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YFinanceTools(stock_price=True, company_info=True, analyst_recommendations=True)],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    instructions=["Use tables to display financial data", "Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

#web_agent.print_response("Find me jobs for role of a solutions architect in united states?", stream=True)
#finance_agent.print_response("Analyze QCOM", stream=True)

app = Playground(agents=[web_agent, finance_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app(app)
