'''
Tests for EcommerceStore model.
'''
import pytest

from scraped.models import ScrapedObject
from scraped.models import EcommerceStore


pytestmark = pytest.mark.django_db


class TestEcommerceStoreModel:
    '''Test cases related to EcommerceStore objects.'''

    def test_create_ecommerce_store(self):
        '''Test creating EcommerceStore object is successful.'''

        assert EcommerceStore.objects.all().count() == 0
        e_store = EcommerceStore.objects.create(
            name='Test Store',
            domain='test-store.com',
            discovery_url='https://test-store.com/',
        )
        assert EcommerceStore.objects.all().count() == 1
        assert isinstance(e_store, EcommerceStore) is True

    def test_ecommerce_store_str_method(self, example_ecommerce_store):
        '''Test that __str__ for EcommerceStore is generating proper output.'''

        e_store = example_ecommerce_store
        assert str(e_store) == e_store.name

    def test_save_method_sets_created_field(self, example_ecommerce_store):
        '''Test save method on class.'''

        e_store = example_ecommerce_store

        assert e_store.created is not None
        assert isinstance(e_store.created, int)
        assert issubclass(EcommerceStore, ScrapedObject)
