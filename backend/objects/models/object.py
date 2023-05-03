from django.db import models


class ScrapedObject(models.Model):
    """Main object for all scraped entities."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_scrape = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
