from django.db import models


class EcommerceStore(models.Model):
    '''EcommerceStore object.'''

    name = models.CharField(max_length=100, unique=True)
    discovery_url = models.CharField(max_length=100, unique=True)
    api_url = models.URLField(max_length=255, blank=True)
    package_name = models.CharField(max_length=50, blank=True)
    module_name = models.CharField(max_length=50, blank=True)
    class_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LocalStore(models.Model):
    '''LocalStore object.'''

    parrent_store = models.ForeignKey(
        EcommerceStore,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=255, blank=True)
    api_url = models.URLField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.parrent_store.name}: {self.name}'
