from rest_framework.serializers import ModelSerializer

from network.models import NetworkLink, Product
from network.validators import CannotUpdateFieldValidator


class NetworkSerializers(ModelSerializer):
    class Meta:
        model = NetworkLink
        fields = "__all__"


class NetworkUpdateSerializers(ModelSerializer):
    class Meta:
        model = NetworkLink
        fields = "__all__"
        validators = [CannotUpdateFieldValidator(field="link_debit")]


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
