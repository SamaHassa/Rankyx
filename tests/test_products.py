import pytest 
from schemas.products import ProductSpecs,SingleExtractedProduct,AllExtractedProducts
from pydantic import ValidationError


def test_product_specs_model():
    product_specs = ProductSpecs(spec_name="Color", spec_value="Red")
    assert product_specs.spec_name == "Color"
    assert product_specs.spec_value == "Red"


def test_product_specs_rejects_empty_name():
    with pytest.raises(ValidationError):
        ProductSpecs(spec_name="", spec_value="Value")

def test_product_specs_rejects_whitespace_name():
    with pytest.raises(ValidationError):
        ProductSpecs(
            spec_name=" ",
            spec_value="Value"
        )

def test_product_specs_rejects_empty_value():
    with pytest.raises(ValidationError):
        ProductSpecs(
            spec_name="RAM",
            spec_value=""
        )


def test_product_specs_rejects_whitespace_value():
    with pytest.raises(ValidationError):
        ProductSpecs(
            spec_name="RAM",
            spec_value=" "
        )

def test_single_extracted_product_valid_data():
    singleproduct=SingleExtractedProduct(page_url="https://store.com/",product_url="https://store.com/laptop",product_title="Gaming Laptop",
            agent_recommendation_rank=1)
    assert str(singleproduct.page_url) == "https://store.com/"
    assert str(singleproduct.product_url) == "https://store.com/laptop"
    assert singleproduct.product_title=="Gaming Laptop"
    assert singleproduct.agent_recommendation_rank==1
    assert singleproduct.product_specs == []
    assert singleproduct.agent_recommendation_notes == []


def test_single_extracted_product_rejects_empty_title():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="",
            agent_recommendation_rank=1
        )
def test_single_extracted_product_rejects_invalid_page_url():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="invalid-url",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            agent_recommendation_rank=1
        )

def test_single_extracted_product_rejects_invalid_product_url():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="invalid-url",
            product_title="Gaming Laptop",
            agent_recommendation_rank=1
        )

def test_single_product_rejects_whitespace_title():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title=" ",
            agent_recommendation_rank=1
        )

def test_single_product_strips_title_whitespace():
    product = SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="  Gaming Laptop  ",
        agent_recommendation_rank=1
    )

    assert product.product_title == "Gaming Laptop"

#1
def test_single_product_accepts_valid_price():
    product = SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_current_price=1500.0,
        agent_recommendation_rank=1
    )

    assert product.product_current_price == 1500

#2
def test_single_product_rejects_zero_price():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            product_current_price=0,
            agent_recommendation_rank=1
        )
#3
def test_single_product_rejects_negative_price():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            product_current_price=-1500,
            agent_recommendation_rank=1
        )

#4
def test_single_product_accepts_none_price():
    product = SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_current_price=None,
        agent_recommendation_rank=1
    )

    assert product.product_current_price is None




def test_single_original_product_accepts_valid_price():
    product = SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=2000.0,
        agent_recommendation_rank=1
    )

    assert product.product_original_price == 2000

def test_single_original_product_rejects_zero_price():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=0,
        agent_recommendation_rank=1
    )

def test_single_original_product_rejects_negative_price():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=-1500,
        agent_recommendation_rank=1
    )

def test_single_original_product_accept_none_price():
        product=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=None,
        agent_recommendation_rank=1)
        assert product.product_original_price is None 

def test_single_product_accepts_valid_rank():
    product=SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            product_original_price=None,
            agent_recommendation_rank=1)
    assert product.agent_recommendation_rank == 1

def test_single_product_rejects_zero_rank():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            product_original_price=None,
            agent_recommendation_rank=0)

def test_single_product_rejects_negative_rank():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
            page_url="https://store.com/",
            product_url="https://store.com/laptop",
            product_title="Gaming Laptop",
            product_original_price=None,
            agent_recommendation_rank=-1)

def test_single_product_accepts_valid_discount():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=3,
                    product_discount_percentage=25.0
    )
    assert product.product_discount_percentage == 25.0

def test_single_product_reject_negative_discount():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=3,
                    product_discount_percentage=-23.0
        )

def test_single_product_reject_greater_than_100_discount():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=3,
                    product_discount_percentage=115
        )


def test_single_product_accepts_none_discount():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=3
    )
    assert product.product_discount_percentage is None

def test_single_product_accepts_100_percent_discount():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=3,
                    product_discount_percentage=100
    )
    assert product.product_discount_percentage ==100

def test_single_product_accepts_zero_discount():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                    product_url="https://store.com/laptop",
                    product_title="Gaming Laptop",
                    product_original_price=None,
                    agent_recommendation_rank=1,
                    product_discount_percentage=0
    )
    assert product.product_discount_percentage == 0

def test_single_product_rejects_more_than_three_specs():
    with pytest.raises(ValidationError):
        SingleExtractedProduct(
        page_url="https://store.com/",
                        product_url="https://store.com/laptop",
                        product_title="Gaming Laptop",
                        product_original_price=None,
                        agent_recommendation_rank=3,
                        product_specs=[
                                ProductSpecs(spec_name="Color", spec_value="Black"),
                                ProductSpecs(spec_name="RAM", spec_value="16GB"),
                                ProductSpecs(spec_name="Storage", spec_value="512GB"),
                                ProductSpecs(spec_name="Processor", spec_value="Intel i7")
                            ])
def test_single_product_accepts_three_specs():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                        product_url="https://store.com/laptop",
                        product_title="Gaming Laptop",
                        product_original_price=None,
                        agent_recommendation_rank=3,
                        product_specs=[
                                ProductSpecs(spec_name="Color", spec_value="Black"),
                                ProductSpecs(spec_name="RAM", spec_value="16GB"),
                                ProductSpecs(spec_name="Storage", spec_value="512GB")
                            ])
    assert len(product.product_specs) == 3

def test_single_product_accepts_empty_specs():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
                                product_url="https://store.com/laptop",
                                product_title="Gaming Laptop",
                                product_original_price=None,
                                agent_recommendation_rank=3
    )
    assert product.product_specs == []

def test_single_product_accepts_none_image_url():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=None,
        agent_recommendation_rank=3
    )
    assert product.product_image_url is None

def test_single_product_accepts_recommendation_notes():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=None,
        agent_recommendation_rank=3,
        agent_recommendation_notes=["Great performance", "Good value for money"]
    )
    assert product.agent_recommendation_notes ==["Great performance", "Good value for money"]


def test_single_product_accepts_recommendation_notes_empty_list():
    product=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop",
        product_title="Gaming Laptop",
        product_original_price=None,
        agent_recommendation_rank=3
    )
    assert product.agent_recommendation_notes ==[]

def test_all_extracted_products_accepts_valid_products():
    product1=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop1",
        product_title="Gaming Laptop 1",
        product_original_price=None,
        agent_recommendation_rank=3
    )
    product2=SingleExtractedProduct(
        page_url="https://store.com/",
        product_url="https://store.com/laptop2",
        product_title="Gaming Laptop 2",
        product_original_price=None,
        agent_recommendation_rank=2
    )
    all_products=AllExtractedProducts(products=[product1,product2])
    assert len(all_products.products) == 2

def test_all_extracted_products_rejects_empty_list():
    with pytest.raises(ValidationError):
        AllExtractedProducts(products=[])

def test_all_extracted_products_rejects_invalid_nested_product():
    with pytest.raises(ValidationError):
        AllExtractedProducts(products=[{
            "page_url": "https://store.com/",
            "product_url": "https://store.com/laptop",
            "product_title": "",
            "agent_recommendation_rank": 1
        
        }])

def test_all_extracted_products_converts_dict_to_product_model():
    all_products = AllExtractedProducts(
    products=[
        {
            "page_url": "https://store.com/",
            "product_url": "https://store.com/laptop1",
            "product_title": "Gaming Laptop 1",
            "agent_recommendation_rank": 3
        }
    ]
)
    assert isinstance(all_products.products[0],SingleExtractedProduct)