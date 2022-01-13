from rest_framework import serializers
from taxi.models import ClientModel, OrderModel, DriverModel


class ClientSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"
        depth = 1

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = '__all__'
