from django.db import models
from django.utils import timezone


class Reserva(models.Model):
    property_id = models.ForeignKey('Propriedade', on_delete=models.CASCADE, related_name='reservas')
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    guests_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.property_id.title} ({self.start_date} a {self.end_date})"

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas' 