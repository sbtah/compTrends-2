from django.db import models
from objects.models.stores import EcommerceStore


class Task(models.Model):
    """
    Abstract class for Task objects.
    """

    class Status(models.TextChoices):
        created = 'CREATED'
        picked_up = 'ACTIVE'
        extended = 'FAILED'
        finished = 'FINISHED'

    store = models.ForeignKey(EcommerceStore, on_delete=models.PROTECT)
    url = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.created,
    )
    created = models.IntegerField()
    last_run = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

class CrawlLocalStores(Task):
    '''
    Class for CrawlLocalStores Task object.
    '''

    class Type(models.TextChoices):
        stores_crawl = 'STORES CRAWL'
    type = models.CharField(
        max_length=30,
        choices=Type.choices,
        default=Type.stores_crawl,
    )
    def __str__(self):
        return f'{self.type}: {self.url}'

class CrawlCategories(Task):
    '''
    Class for CrawlCategories object.
    '''

    class Type(models.TextChoices):
        categories_crawl = 'CATEGORIES CRAWL'

    type = models.CharField(
        max_length=30,
        choices=Type.choices,
        default=Type.categories_crawl,
    )
    category_level = models.IntegerField()

    def __str__(self):
        return f'{self.type}: {self.url}'

class CrawlProducts(Task):
    """
    Class for CrawlProducts object.
    """

    class Type(models.TextChoices):
        products_crawl = 'PRODUCTS CRAWL'

    type = models.CharField(
        max_length=30,
        choices=Type.choices,
        default=Type.products_crawl,
    )
    category_level = models.IntegerField()

    def __str__(self):
        return f'{self.type}: {self.url}'

class ScrapeProduct(Task):
    """"""
    class Type(models.TextChoices):
        product_scrape = 'PRODUCT SCRAPE'

    type = models.CharField(
        max_length=30,
        choices=Type.choices,
        default=Type.product_scrape,
    )

    def __str__(self):
        return f'{self.type}: {self.url}'
