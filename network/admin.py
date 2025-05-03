from django.contrib import admin
from network.models import Company, Product, Network


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс Product в административной панели"""

    list_display = ('pk', 'name', 'model', 'started_date')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Класс Company в административной панели"""

    list_display = ('pk', 'name', 'company_level', 'email', 'country', 'city', 'street', 'build_number')
    list_filter = ('city',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Класс Network в административной панели"""

    list_display = ('pk', 'link', 'link_level', 'link_product', 'link_supplier', 'link_debit', 'link_created_at', 'user')
