from django.contrib import admin
from objects.models.stores import EcommerceStore, LocalStore
from objects.models.tasks import Task


admin.site.register(EcommerceStore)
admin.site.register(LocalStore)

admin.site.register(Task)
