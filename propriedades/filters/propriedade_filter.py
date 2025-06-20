"""Módulo propriedade_filter."""

from django_filters import rest_framework as filters

from ..models import Propriedade


class PropriedadeFilter(filters.FilterSet):
    address_city = filters.CharFilter(lookup_expr='icontains')
    address_state = filters.CharFilter(lookup_expr='icontains')
    country = filters.CharFilter(lookup_expr='iexact')
    capacity = filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    price_per_night = filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')

    class Meta:
        model = Propriedade
        fields = [
            'address_city',
            'address_state',
            'country',
            'capacity',
            'price_per_night'
        ]
