from rest_framework.serializers import ModelSerializer

from network.models import NetworkLink, Product


class NetworkSerializers(ModelSerializer):
    class Meta:
        model = NetworkLink
        fields = "__all__"


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
