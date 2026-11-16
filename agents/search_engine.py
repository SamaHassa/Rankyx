# ==========================
#     Agent 2:Search Engine
# ==========================

from config import llm
from crewai import Agent,Task
from schemas.search import SearchEngineOutput
from tools.search_tool import search_engine_tool

search_engine_agent = Agent(
    role="E-commerce Search Specialist",
    goal=(
    "Search for relevant product listings using the generated queries. "
    "Return accurate results from the requested websites, prioritizing "
    "product pages with useful pricing and specifications."
),
    backstory=(
    "You are skilled at web research and product discovery. "
    "You identify relevant listings, reject irrelevant pages, "
    "and preserve source information accurately."
),
    llm=llm,
    verbose=True,
    tools=[search_engine_tool]
)

search_engine_task=Task(
    name="Search Engine Task",
    description=(
    "Use the generated queries to find product listings on "
    "{websites_list}. Return relevant results containing title, URL, "
    "content, confidence score, and search query. Exclude results "
    "below {score_threshold}. Prioritize product pages."
),
    expected_output="A structured JSON object containing the search results for each query.",
    output_pydantic=SearchEngineOutput,
    output_file="agent-output/search_engine_results.json",
    agent=search_engine_agent
)
