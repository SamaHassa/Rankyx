from agents.search_query import search_agent,search_agent_task
from agents.search_engine import search_engine_agent,search_engine_task
from agents.scraping import scraping_agent,scraping_task
from agents.report_generation import report_agent,report_task
from crewai import Crew,Process
import logging


logger=logging.getLogger(__name__)

def run_research(inputs):

    crew = Crew(
        agents=[search_agent, search_engine_agent,scraping_agent, report_agent],
        tasks=[search_agent_task, search_engine_task, scraping_task, report_task],
        process=Process.sequential,
        verbose=True
    )
    try:
        crew_results = crew.kickoff(
            inputs=inputs
        )
    except Exception :
        logger.exception("An error occurred while running the research workflow.")
        crew_results = "Sorry, we couldn't complete your product research. Please try again."

    return crew_results



# "product_name": "iPhone 14",
#           "websites_list": ", ".join(["Amazon", "eBay", "Walmart"]),
#           "country_name": "Egypt",
#           "no_keywords": no_keywords,
#           "language": "English",
#           "score_threshold": 0.5,
#           "top_recommendations_no": 5