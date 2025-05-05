from rest_framework import generics
from network.models import NetworkLink, Product
from network.serializers import NetworkSerializers, ProductSerializers, NetworkUpdateSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    """Создание объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Обновление объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class NetworkLinkCreateAPIView(generics.CreateAPIView):
    """Создание объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers


class NetworkLinkUpdateAPIView(generics.UpdateAPIView):
    """Обновление объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkUpdateSerializers


class NetworkLinkRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers


class NetworkLinkListAPIView(generics.ListAPIView):
    """Просмотр списка объектов Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers


class NetworkLinkDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers
