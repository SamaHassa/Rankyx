from config import scrapegraph_client
import json
from schemas.products import SingleExtractedProduct
from crewai.tools import tool


@tool
def scraping_tool(url: str) -> str:
    """Extract product information from one ecommerce product page."""

    result = scrapegraph_client.extract(
        prompt=(
            "Extract product title, product URL, image URL, current price, "
            "original price, discount percentage, and up to 3 specifications. "
            "Do not invent missing values."
        ),
        url=url,
        schema=SingleExtractedProduct.model_json_schema()
    )

    return json.dumps({
        "page_url": url,
        "details": result.data
    }, default=str)