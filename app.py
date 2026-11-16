import os
from services.research_workflow import run_research

os.makedirs("agent-output", exist_ok=True)

no_keywords = 2

#==============================
#             Run Crew
#==============================

results=run_research(inputs={"product_name": "iPhone 14",
            "websites_list": ", ".join(["Amazon", "eBay", "Walmart"]),
            "country_name": "Egypt",
            "no_keywords": no_keywords,
            "language": "English",
            "score_threshold": 0.5,
            "top_recommendations_no": 5})

print(results)