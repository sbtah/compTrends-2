'''
Tests for Category model.
'''
import pytest
from scraped.models import Category
from scraped.models import ScrapedObject


pytestmark = pytest.mark.django_db


class TestCategoryModel:
    '''Test cases related to Category objects.'''

    def test_create_category(self, example_ecommerce_store):
        '''Test creating Category objects is successful'''

        assert Category.objects.all().count() == 0
        e_store = example_ecommerce_store
        name = 'Test Category'
        url = 'https://test-store/test-category'
        category = Category.objects.create(
            parrent_store=e_store,
            name=name,
            url=url,
        )
        assert Category.objects.all().count() == 1
        assert isinstance(category, Category)

    def test_category_str_method(self, example_category):
        '''Test that __str__ for Category is generating proper output.'''

        category = example_category
        assert str(category) == category.name

    def test_save_method_sets_created_field(self, example_category):
        '''Test save method on class'''

        category = example_category
        assert category.created is not None
        assert isinstance(category.created, int)
        assert issubclass(Category, ScrapedObject)
