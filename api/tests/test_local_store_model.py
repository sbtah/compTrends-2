'''
Tests for LocalStore model.
'''
import pytest
from scraped.models import LocalStore
from scraped.models import ScrapedObject


pytestmark = pytest.mark.django_db


class TestLocalStoremodel:
    '''Test cases related to LocalStore objects.'''

    def test_create_local_store(self, example_ecommerce_store):
        '''Test creating LocalStore object is successful.'''

        assert LocalStore.objects.all().count() == 0
        e_store = example_ecommerce_store
        local_store = LocalStore.objects.create(
            parrent_store=e_store,
            name='New York',
            scraped_id=1,
            is_active=True,
        )
        assert LocalStore.objects.all().count() == 1
        assert isinstance(local_store, LocalStore) is True

    def test_local_store_str_method(self, example_local_store):
        '''Test that __str__ for LocalStore is properly generated.'''

        local_store = example_local_store
        assert str(local_store) == f'{local_store.parrent_store.name}: {local_store.name}' # noqa

    def test_save_method_sets_created_field(self, example_local_store):
        '''Test save method on class.'''

        local_store = example_local_store

        assert local_store.created is not None
        assert isinstance(local_store.created, int)
        assert issubclass(LocalStore, ScrapedObject)
