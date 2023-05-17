from django.db import models
from objects.models.stores import EccommerceStore
from objects.models.objects import ScrapedObject


class Category(ScrapedObject):
    """Category object."""

    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    api_url = models.URLField(max_length=255, blank=True)
    scraped_id = models.IntegerField(null=True)
    category_level = models.IntegerField(null=True)
    product_count = models.IntegerField(null=True)
    parrent_store = models.ForeignKey(
        EccommerceStore,
        on_delete=models.CASCADE,
    )
    child_categories = models.ManyToManyField("self")
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class CategoryExtraField(models.Model):
    """
    Extra field for Category object,
    used if we want to extend model with extra data.
    """

    parrent_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    field_name = models.CharField(max_length=100)
    field_data = models.TextField()

    def __str__(self):
        return self.field_name
