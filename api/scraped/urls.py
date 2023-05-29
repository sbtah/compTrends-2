from django.urls import path
from scraped import views


app_name = 'scraped'


urlpatterns = [
    path(
        'stores/',
        views.ecommerce_store_list_view,
        name="store-list",
    ),
    path(
        'create/',
        views.ecommerce_store_create_view,
        name="store-create",
    ),
    path(
        'stores/<int:pk>/',
        views.ecommerce_store_detail_view,
        name='store-detail',
    ),
    path(
        'stores/<int:pk>/update/',
        views.ecommerce_store_update_view,
        name='store-update',
    ),
    path(
        'stores/<int:pk>/delete/',
        views.ecommerce_store_delete_view,
        name='store-delete',
    ),
]