"""Módulo propriedade_viewset."""

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from ..filters import PropriedadeFilter
from ..models import Propriedade
from ..serializers import PropriedadeSerializer


class PropriedadeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar propriedades.
    Permite CRUD completo e filtros por localização, capacidade e preço.
    """
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropriedadeFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        nome = instance.title  # ou instance.nome, dependendo do campo
        self.perform_destroy(instance)
        return Response(
            {"message": f"Propriedade '{nome}' deletada."},
            status=status.HTTP_200_OK
        )
