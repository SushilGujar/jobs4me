from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["List the links to apply for the jobs in a table format"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Find me job posts for role of a solutions architect in Tennessee?", stream=True)