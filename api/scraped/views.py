from rest_framework import authentication, generics, mixins
from scraped.models import EcommerceStore
from scraped.serializers import EcommerceStoreSerializer, EcommerceStoreDetailSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EcommerceStoreListAPIView(generics.ListAPIView):
    '''List Api View for EcommerceStore.'''

    serializer_class = EcommerceStoreSerializer
    queryset = EcommerceStore.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.order_by("-id")

ecommerce_store_list_view = EcommerceStoreListAPIView.as_view()


class EcommerceStoreDetailAPIView(generics.RetrieveAPIView):
    '''Detail Api View for EcommerceStore.'''

    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

ecommerce_store_detail_view = EcommerceStoreDetailAPIView.as_view()


class EcommerceStoreCreateAPIView(generics.CreateAPIView):
    '''Create Api View for EcommerceStore.'''

    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

ecommerce_store_create_view = EcommerceStoreCreateAPIView.as_view()


class EcommerceStoreUpdateAPIView(generics.UpdateAPIView):
    '''Update Api View for EcommerceStore.'''

    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

ecommerce_store_update_view = EcommerceStoreUpdateAPIView.as_view()


class EcommerceStoreDeleteAPIView(generics.DestroyAPIView):
    '''Delete Api View for EcommerceStore.'''

    queryset = EcommerceStore.objects.all()
    serializer_class = EcommerceStoreDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

ecommerce_store_delete_view = EcommerceStoreDeleteAPIView.as_view()