"""Módulo reserva_serializer."""

from rest_framework import serializers

from ..models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            'id', 'property_id', 'client_name', 'client_email', 'start_date',
            'end_date', 'guests_quantity', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
