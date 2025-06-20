"""Módulo reserva_service."""

from propriedades.models import Propriedade

from rest_framework import status
from rest_framework.response import Response

from ..models import Reserva


class ReservaService:
    @staticmethod
    def validar_e_criar_reserva(data):
        """
        Valida e cria uma reserva se todas as condições forem atendidas.
        Retorna (sucesso, resposta) onde sucesso é um booleano.
        """
        property_id = data.get('property_id')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        guests_quantity = int(data.get('guests_quantity', 0))

        # Verificar se a propriedade existe
        try:
            propriedade = Propriedade.objects.get(id=property_id)
        except Propriedade.DoesNotExist:
            return False, Response(
                {'error': 'Propriedade não encontrada'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verificar capacidade
        if guests_quantity > propriedade.capacity:
            return False, Response(
                {'error': 'Número de hóspedes excede a capacidade máxima da propriedade'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verificar disponibilidade
        reservas_existentes = Reserva.objects.filter(
            property_id=propriedade,
            start_date__lt=end_date,
            end_date__gt=start_date
        )

        if reservas_existentes.exists():
            return False, Response(
                {'error': 'A propriedade não está disponível para o período solicitado'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Se chegou até aqui, pode criar a reserva
        return True, None
