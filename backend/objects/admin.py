from django.contrib import admin
from objects.models.stores import EcommerceStore, LocalStore
from objects.models.tasks import CrawlCategories, CrawlProducts, ScrapeProduct


admin.site.register(EcommerceStore)
admin.site.register(LocalStore)

admin.site.register(CrawlCategories)
admin.site.register(CrawlProducts)
admin.site.register(ScrapeProduct)