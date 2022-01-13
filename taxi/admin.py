from django.contrib import admin

from taxi.models import ClientModel, DriverModel, OrderModel

admin.site.register(ClientModel)
admin.site.register(DriverModel)
admin.site.register(OrderModel)