from dotenv import load_dotenv
import os
from crewai import LLM
from tavily import TavilyClient
from scrapegraph_py import ScrapeGraphAI
import agentops
load_dotenv()


agentops.init(
  os.environ.get("AGENTOPS_API_KEY"),
)

tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

scrapegraph_client = ScrapeGraphAI(api_key=os.environ.get("SCRAPGRAPH_API_KEY"))


llm = LLM(
    model="openai/openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0
)