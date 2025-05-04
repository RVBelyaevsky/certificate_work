from django.contrib import admin
from network.models import NetworkLink, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс Product в административной панели"""

    list_display = ('pk', 'name', 'model', 'started_date', 'supplier')


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    """Класс NetworkLink в административной панели"""

    list_display = ('pk', 'name', 'link_level', 'email', 'country', 'city', 'street', 'build_number', 'supplier', 'link_debit', 'link_created_at', 'user')
