# ==========================
#     Agent 4:Report
# ==========================


from config import llm
from crewai import Agent,Task
from schemas.products import AllExtractedProducts
from tools.scraping_tool import scraping_tool
from agents.scraping import scraping_task

report_agent = Agent(
    role="Product Comparison Report Generator",
    goal=(
    "Generate a professional, standalone HTML report comparing "
    "the extracted products using only verified input data."
),

    backstory=(
    "You specialize in presenting product research through clean, "
    "responsive HTML reports. You prioritize clarity, accurate "
    "comparisons, and evidence-based recommendations."
),

    llm=llm,
    verbose=False
)


report_task = Task(
    name="Report Generation Task",

    description=(
    "Create a standalone HTML report containing an executive summary, "
    "product comparison table, specifications, price analysis, "
    "advantages, disadvantages, recommendations, and data limitations. "
    "Include source links when available. Use responsive CSS and "
    "Bootstrap. Return complete HTML only. Never invent information."
),

    expected_output=(
        "A complete, standalone HTML report styled with CSS and Bootstrap, "
        "ready to open in a web browser."
    ),

    context=[scraping_task],#context of the report task is the output of the scraping task
    output_file="agent-output/product_report.html",
    agent=report_agent
)