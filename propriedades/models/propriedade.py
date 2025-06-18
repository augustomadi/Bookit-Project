from django.db import models
from django.utils import timezone


class Propriedade(models.Model):
    title = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)
    address_number = models.CharField(max_length=20)
    address_neighborhood = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=2)
    country = models.CharField(max_length=3, default='BRA')
    rooms = models.IntegerField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades' 