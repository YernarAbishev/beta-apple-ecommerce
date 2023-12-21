from django.db import models
from ecommerce.apps.catalog.models import Product

class Order(models.Model):
    full_name = models.CharField("Толық аты", max_length=75)
    email = models.EmailField("E-mail", max_length=40)
    city = models.CharField("Қала", max_length=30)
    address = models.CharField("Мекен-жайы", max_length=120)
    phone = models.CharField("Телефон", max_length=10)
    payment12 = models.BooleanField("Рассрочка 0:0:12", default=False)
    card_payment = models.BooleanField("Картамен төлем", default=False)
    card_number = models.CharField("Карта нөмірі", max_length=255, null=True, blank=True)
    card_date = models.CharField("Карта мерзімі", max_length=255, null=True, blank=True)
    card_cvv = models.CharField("Карта cvv", max_length=10, null=True, blank=True)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тапсырыс"
        verbose_name_plural = "Тапсырыстар"
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Тапсырыс тауары"
        verbose_name_plural = "Тапсырыс тауарлары"


    def __str__(self):
        return f"{self.id} - {self.order.full_name}"

