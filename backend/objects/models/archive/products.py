from django.db import models
from objects.models.objects import ScrapedObject
from backend.objects.models.archive.categories import Category
from objects.models.stores import EccommerceStore


class Product(ScrapedObject):
    """Product object."""

    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, unique=True, db_index=True)
    scraped_id = models.IntegerField(unique=True, db_index=True)
    type_id = models.CharField(max_length=100, blank=True)
    api_url = models.URLField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    sku = models.CharField(max_length=50, blank=True)
    ean = models.CharField(max_length=50, blank=True)
    brand_name = models.CharField(max_length=50, blank=True)
    promotion = models.BooleanField(default=False)

    default_price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2,
    )
    promo_price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2,
    )

    unit_type = models.CharField(max_length=10, blank=True)
    conversion = models.CharField(max_length=10, blank=True)
    conversion_unit = models.CharField(max_length=10, blank=True)
    qty_per_package = models.IntegerField(null=True)
    tax_rate = models.CharField(max_length=10, blank=True)
    parrent_category_from_path = models.IntegerField(null=True)
    parrent_store = models.ForeignKey(
        EccommerceStore,
        on_delete=models.CASCADE,
    )
    parrent_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductLocalData(ScrapedObject):
    """ProductLocalData object."""

    parrent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parrent_product_scraped_id = models.IntegerField()
    # TODO:
    # Change to relation
    local_store_name = models.CharField(max_length=255)
    local_store_scraped_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2,
    )
    type_id = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(null=True)
    stock_status = models.IntegerField(null=True)
    availability = models.CharField(max_length=10, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["parrent_product", "local_store_name", "last_scrape"],
                name="Unique ProductLocalData",
            ),
        ]
        verbose_name_plural = "Product Local Data"

    def __str__(self):
        return f"{self.local_store_name}: {self.name}"


class ProductExtraField(models.Model):
    """
    Extra field for Product object,
    used if we want to extend model with extra data.
    """

    parrent_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    field_name = models.CharField(max_length=100)
    field_data = models.TextField()

    def __str__(self):
        return f"{self.parrent_product.name}: {self.field_name}"