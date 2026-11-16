# ==========================
#     Agent 3:Scraping
# ==========================

from config import llm
from crewai import Agent,Task
from schemas.products import AllExtractedProducts
from tools.scraping_tool import scraping_tool

scraping_agent=Agent(
    role="E-commerce Product Data Extractor",  
    goal=(
    "Extract accurate product information by calling scraping_tool "
    "with one product page URL per call. Never invent missing data."
),
    backstory=(
    "You specialize in extracting structured product information "
    "from e-commerce pages. You prioritize accuracy, source traceability, "
    "and clearly identifying unavailable information."
),    llm=llm,
    verbose=False,
    tools=[scraping_tool]
) 

scraping_task=Task(
    name="Scraping Task",
    description=(
    "Extract the top {top_recommendations_no} relevant products "
    "from the search results. Use scraping_tool for each product URL. "
    "Collect the title, URL, image, prices, discount, and up to "
    "3 specifications. Do not fabricate missing values."
),
    expected_output="A structured JSON object containing the extracted product information from the scraped product listings.",
    output_pydantic=AllExtractedProducts,
    output_file="agent-output/scraping_results.json",
    agent=scraping_agent
)
