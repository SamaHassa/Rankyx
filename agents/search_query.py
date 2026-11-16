# ==========================
#     Agent 1:Search Query
# ==========================

from config import llm
from crewai import Agent,Task
from schemas.search import SearchQueryOutput




search_agent = Agent(
    role="E-commerce Search Strategist",
    goal=(
    "Generate up to {no_keywords} distinct, concise English search "
    "queries for {product_name}. Target product pages on {websites_list} "
    "in {country_name}. Write each query as a question and focus on "
    "different product specifications or brands."
),
    backstory=(
    "You specialize in e-commerce search. You understand product "
    "specifications, brands, and shopping intent. Avoid duplicate "
    "queries and irrelevant results."
),
    llm=llm,
    verbose=False
)



search_agent_task = Task(
    name="Search Query Generation",
    description=(
    "Generate up to {no_keywords} relevant English search queries "
    "for {product_name}. Target {websites_list} in {country_name}. "
    "Focus on distinct product-page search angles."
),
    expected_output=(
        "A structured JSON object containing a list of "
        "relevant ecommerce search queries."
    ),
    output_pydantic=SearchQueryOutput,
    output_file="agent-output/search_queries.json",
    agent=search_agent
)



