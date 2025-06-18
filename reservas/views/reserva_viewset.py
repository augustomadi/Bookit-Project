from rest_framework import viewsets
from ..models import Reserva
from ..serializers import ReservaSerializer
from ..services import ReservaService
from rest_framework.response import Response
from rest_framework import status
from ..filters import ReservaFilter
from django_filters.rest_framework import DjangoFilterBackend

class ReservaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar reservas.
    Inclui validações de disponibilidade e capacidade.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservaFilter
    
    def create(self, request, *args, **kwargs):
        """
        Cria uma nova reserva após validar disponibilidade e capacidade.
        """
        # Usar o service para validar
        sucesso, resposta_erro = ReservaService.validar_e_criar_reserva(request.data)
        
        if not sucesso:
            return resposta_erro
        
        # Se passou por todas as validações, criar a reserva
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        cliente = instance.client_name
        self.perform_destroy(instance)
        return Response(
            {"message": f"Reserva de {cliente} cancelada com sucesso."},
            status=status.HTTP_200_OK
        ) 