from django_filters import rest_framework as filters
from ..models import Reserva

class ReservaFilter(filters.FilterSet):
    client_email = filters.CharFilter(field_name='client_email', lookup_expr='iexact')
    property_id = filters.NumberFilter(field_name='property_id')

    class Meta:
        model = Reserva
        fields = ['client_email', 'property_id']