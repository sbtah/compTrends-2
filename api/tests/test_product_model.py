'''
Tests for Product model.
'''
import pytest
from scraped.models import Product
from scraped.models import ScrapedObject


pytestmark = pytest.mark.django_db


class TestProductModel:
    '''Test cases related to Category objects.'''

    def test_create_product(self, example_ecommerce_store):
        '''Test creating Product object is successful.'''

        assert Product.objects.all().count() == 0
        e_store = example_ecommerce_store
        name = 'Test Product'
        url = 'https://test-store/test-product'
        product = Product.objects.create(
            parrent_store=e_store,
            name=name,
            url=url,
        )
        assert Product.objects.all().count() == 1
        assert isinstance(product, Product)

    def test_product_str_method(self, example_product):
        '''Test that __str__ for Product is generating proper output.'''

        product = example_product
        assert str(product) == product.name

    def test_save_method_sets_created_field(self, example_product):
        '''Test save method on class'''

        product = example_product
        assert product.created is not None
        assert isinstance(product.created, int)
        assert issubclass(Product, ScrapedObject)
