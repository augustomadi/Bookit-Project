from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Propriedade, Reserva

class PropertyAvailabilityView(APIView):
    def get(self, request):
        property_id = request.GET.get('property_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        guests_quantity = int(request.GET.get('guests_quantity', 0))

        # Verifica se a propriedade existe
        try:
            propriedade = Propriedade.objects.get(id=property_id)
        except Propriedade.DoesNotExist:
            return Response({'available': False, 'error': 'Propriedade não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Verifica capacidade
        if guests_quantity > propriedade.capacity:
            return Response({'available': False, 'error': 'Número de hóspedes excede a capacidade máxima.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica disponibilidade
        reservas_existentes = Reserva.objects.filter(
            property_id=propriedade,
            start_date__lt=end_date,
            end_date__gt=start_date
        )
        if reservas_existentes.exists():
            return Response({'available': False, 'error': 'Propriedade indisponível para o período solicitado.'}, status=status.HTTP_200_OK)

        return Response({'available': True}, status=status.HTTP_200_OK)