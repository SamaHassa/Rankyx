
from pydantic import BaseModel, Field, field_validator,HttpUrl


class ProductSpecs(BaseModel):
    spec_name: str = Field(..., min_length=1)
    spec_value: str = Field(..., min_length=1)

    @field_validator("spec_name", "spec_value")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Specification fields cannot be blank")
        return value

class SingleExtractedProduct(BaseModel):
    page_url: HttpUrl = Field(..., min_length=1)
    product_title: str = Field(..., min_length=1)

    @field_validator("product_title")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Product title cannot be blank")
        return value
    product_url: HttpUrl = Field(..., min_length=1)
    product_image_url: HttpUrl | None = None
    product_current_price: float | None = Field(default=None, gt=0)
    product_original_price: float | None = Field(default=None, gt=0)
    product_discount_percentage: float | None = Field(default=None, ge=0, le=100)
    product_specs: list[ProductSpecs] = Field(default_factory=list, max_length=3)
    agent_recommendation_rank: int = Field(..., ge=1)
    agent_recommendation_notes: list[str] = Field(default_factory=list)


class AllExtractedProducts(BaseModel):
    products: list[SingleExtractedProduct] = Field(..., min_length=1)
