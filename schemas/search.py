from pydantic import BaseModel,Field,HttpUrl

class SearchQueryOutput(BaseModel):
    queries: list[str] = Field(
        ...,
        description="List of generated search queries",
        min_length=1,
        max_length=3
    )


class SingleSearchResult(BaseModel):
    title: str = Field(..., min_length=1)
    url: HttpUrl = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    score: float = Field(..., ge=0, le=1)   # ge/le OK here (a number)
    search_query: str = Field(..., min_length=1)

class SearchEngineOutput(BaseModel):
    search_results: list[SingleSearchResult] = Field(
        ...,
        description="List of search results for each query",
        min_length=1,
        max_length=3
    )


