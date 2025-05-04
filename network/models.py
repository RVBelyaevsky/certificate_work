from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class NetworkLink(models.Model):
    """Модель торговой сети"""

    LINK_LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=150, verbose_name='название звена')
    link_level = models.IntegerField(choices=LINK_LEVEL_CHOICES, verbose_name='уровень звена сети')

    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='улица', **NULLABLE)
    build_number = models.IntegerField(verbose_name='номер дома', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик звена', **NULLABLE)
    link_debit = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, verbose_name='задолженность звена')
    link_created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель звена')

    def __str__(self):
        return f"network link {self.name}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):
    """Модель товара для сети по продаже электронной техники"""

    name = models.CharField(max_length=150, verbose_name='название товара')
    model = models.CharField(max_length=150, verbose_name='модель товара')
    started_date = models.DateField(verbose_name='дата выхода товара на рынок')

    supplier = models.ForeignKey(NetworkLink, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return f" product {self.name}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
