from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment

job_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    #model=Groq(id="llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4-1106-preview"),
    tools=[DuckDuckGo()],
    instructions=["list top 10 job posts in table format with the columns Company, Job Title, Location, Base Salary, and exact URL to apply",
                    "Only consider the jobs posted in last one month",],
    show_tool_calls=True,
    markdown=True,
)
job_agent.print_response("Find principal solutions architect job posts in United States.", stream=True)


