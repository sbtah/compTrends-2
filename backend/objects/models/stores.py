from django.db import models
from objects.models.object import ScrapedObject


class EccommerceStore(ScrapedObject):
    """EccommerceStore object."""

    domain = models.CharField(max_length=100, unique=True)
    main_url = models.CharField(max_length=100, unique=True)
    # Url from which Scraper will start discovery of Categories.
    discovery_url = models.CharField(max_length=100, unique=True)
    api_url = models.URLField(max_length=255, blank=True)
    module_name = models.CharField(max_length=50, blank=True)
    class_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.domain


class LocalStore(ScrapedObject):
    """LocalStore object, child of EcommerceStore."""

    parrent_store = models.ForeignKey(
        EccommerceStore,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, unique=True)
    scraped_id = models.IntegerField(null=True)
    url = models.URLField(max_length=255, blank=True)
    api_url = models.URLField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.scraped_id}: {self.name}"


class StoreExtraField(ScrapedObject):
    """
    Extra field for EccommerceStore,
    used if we want to extend model with extra data.
    """

    parrent_store = models.ForeignKey(
        EccommerceStore,
        on_delete=models.CASCADE,
    )
    field_name = models.CharField(max_length=100)
    field_data = models.TextField()

    def __str__(self):
        return self.field_name
