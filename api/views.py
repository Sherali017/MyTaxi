from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from taxi.models import ClientModel, OrderModel, DriverModel, user
from .serializers import ClientSerializerGet, ClientSerializer, DriverSerializer, OrderSerializer
from rest_framework.decorators import api_view


def get_object(Model, pk):
    try:
        return Model.objects.get(id=pk)
    except:
        return None


@api_view(["POST"])
def orderCreate(request, pk=None):
    queryset = get_object(OrderModel, pk)
    if queryset:
        serializer = ClientSerializer(data=request.data, instance=queryset)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response("POST")


# class OrderViewSet(viewsets.ViewSet):
#     def order(self, request):
#         queryset = OrderModel.objects.all()
#         serializer = OrderSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def api_order_get_view(request, slug):
    try:
        Order = OrderModel.objects.get(slug=slug)
    except OrderModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(Order)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_order_view(request, slug):
    try:
        Order = OrderModel.objects.get(slug=slug)
    except OrderModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializer(Order, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succes"] = "update succesful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', ])
def api_delete_order_view(request, slug):
    try:
        Order = OrderModel.objects.get(slug=slug)
    except OrderModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = OrderModel.delete()
        data = {}
        if operation:
            data["succes"] = "delete succesful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
