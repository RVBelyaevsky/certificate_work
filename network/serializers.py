from rest_framework.serializers import ModelSerializer

from network.models import Network, Company, Product


class NetworkSerializers(ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"


class CompanySerializers(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
