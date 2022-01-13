from django.urls import path

from api.views import orderCreate, api_order_get_view, api_update_order_view, api_delete_order_view

urlpatterns = [
    path('order/',orderCreate),
    path('order_get/', api_order_get_view),
    path('order_update', api_update_order_view),
    path('order_delete', api_delete_order_view)
]