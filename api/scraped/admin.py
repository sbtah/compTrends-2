from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from scraped.models import EcommerceStore, LocalStore


class EcommerceStoreAdmin(admin.ModelAdmin):
    '''Admin for EcommerceStore object.'''

    ordering = ['id']
    list_display = [
        'name',
        'domain',
        'last_scrape_start',
        'last_scrape_end',
        'is_active',
        'is_monitored',
        ]
    fieldsets = (
        (None, {'fields': ('name', 'domain', 'discovery_url')}),
        (
            _('Scraper Import'),
            {'fields': ('package_name', 'module_name', 'class_name')}
        ),
        (
            _('Dates'),
            {'fields': ('created', 'last_scrape_start', 'last_scrape_end')}
        ),
        (_('Status'), {'fields': ('is_active', 'is_monitored')}),
    )
    readonly_fields = ['created', 'last_scrape_start', 'last_scrape_end']


class LocalStoreAdmin(admin.ModelAdmin):
    '''Admin for LocalStore object.'''

    ordering = ['id']
    list_display = [
        'name',
        'scraped_id',
        'last_scrape_start',
        'last_scrape_end',
        'is_active',
        'is_monitored',
        'parrent_store',
        ]
    fieldsets = (
        (
            None,
            {'fields': (
                'parrent_store',
                'name',
                'scraped_id',
                'url',
                'api_url',
            )},
        ),
        (
            _('Dates'),
            {'fields': ('created', 'last_scrape_start', 'last_scrape_end')}
        ),
        (_('Status'), {'fields': ('is_active', 'is_monitored')}),
    )
    readonly_fields = [
        'created',
        'last_scrape_start',
        'last_scrape_end',
        'parrent_store'
        ]



admin.site.register(EcommerceStore, EcommerceStoreAdmin)
admin.site.register(LocalStore, LocalStoreAdmin)
