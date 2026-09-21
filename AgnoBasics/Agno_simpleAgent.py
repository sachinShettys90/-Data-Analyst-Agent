from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


agent = Agent(
    name="Finance Agent",
    role="Get webbased data",
    model=OpenAIChat(id="gpt-4o"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    markdown=True
)

agent.print_response("Who won the India vs Newzealand finals in CT 2025")
