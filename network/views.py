from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from network.models import NetworkLink, Product
from network.permissions import IsActive
from network.serializers import NetworkSerializers, ProductSerializers, NetworkUpdateSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    """Создание объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Обновление объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsActive]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsActive]


class NetworkLinkCreateAPIView(generics.CreateAPIView):
    """Создание объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers


class NetworkLinkUpdateAPIView(generics.UpdateAPIView):
    """Обновление объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkUpdateSerializers
    permission_classes = [IsActive]


class NetworkLinkRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers
    permission_classes = [IsActive]


class NetworkLinkListAPIView(generics.ListAPIView):
    """Просмотр списка объектов Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['country']


class NetworkLinkDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта Network"""

    queryset = NetworkLink.objects.all()
    serializer_class = NetworkSerializers
    permission_classes = [IsActive]
