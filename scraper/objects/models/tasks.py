from django.db import models
from objects.models.stores import EcommerceStore


class Task(models.Model):
    '''Abstract class for Task objects.'''

    class Status(models.TextChoices):
        created = 'CREATED'
        picked_up = 'ACTIVE'
        extended = 'FAILED'
        finished = 'FINISHED'

    class Type(models.TextChoices):
        local_stores_crawl = 'STORES-CRAWL'
        categories_crawl = 'CATEGORIES-CRAWL'
        products_crawl = 'PRODUCTS-CRAWL'
        products_scrape = 'PRODUCT-SCRAPE'
        product_local_data_scrape = 'PRODUCTLOCALDATA-SCRAPE'


    store = models.ForeignKey(
        EcommerceStore,
        on_delete=models.PROTECT
    )
    url = models.URLField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.created,
    )
    type = models.CharField(
        max_length=40,
        choices=Type.choices,
    )
    category_level = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()
    started_at = models.IntegerField(blank=True, null=True)
    finished_at = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.type}: {self.url}'
