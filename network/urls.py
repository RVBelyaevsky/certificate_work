from django.urls import path
from network.apps import NetworkConfig
from network.views import NetworkLinkListAPIView, NetworkLinkRetrieveAPIView, NetworkLinkCreateAPIView, \
    NetworkLinkUpdateAPIView, NetworkLinkDestroyAPIView, ProductCreateAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('', NetworkLinkListAPIView.as_view(), name='network_list'),
    path('<int:pk>/', NetworkLinkRetrieveAPIView.as_view(), name='network_retrieve'),
    path('create/', NetworkLinkCreateAPIView.as_view(), name='network_create'),
    path('update/<int:pk>/', NetworkLinkUpdateAPIView.as_view(), name='network_update'),
    path('destroy/<int:pk>/', NetworkLinkDestroyAPIView.as_view(), name='network_destroy'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
]
