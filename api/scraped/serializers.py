from rest_framework import serializers
from rest_framework.reverse import reverse
from scraped.models import EcommerceStore


class EcommerceStoreSerializer(serializers.ModelSerializer):
    '''Serializer for EcommerceStore.'''

    class Meta:
        model = EcommerceStore
        fields = [
            'id',
            'name',
            'domain',
        ]
        read_only_fields = ['id',]


class EcommerceStoreDetailSerializer(EcommerceStoreSerializer):
    '''Detail serializer for EcommerceStore detail view.'''

    class Meta(EcommerceStoreSerializer.Meta):
        fields = EcommerceStoreSerializer.Meta.fields + [
            'discovery_url',
            'package_name',
            'module_name',
            'class_name',
            'created',
            'last_scrape_start',
            'last_scrape_end',
            'is_active',
            'is_monitored',
        ]