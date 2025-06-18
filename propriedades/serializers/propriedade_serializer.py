from rest_framework import serializers
from ..models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = [
            'id', 'title', 'address_street', 'address_number', 'address_neighborhood',
            'address_city', 'address_state', 'country', 'rooms', 'capacity',
            'price_per_night', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at'] 