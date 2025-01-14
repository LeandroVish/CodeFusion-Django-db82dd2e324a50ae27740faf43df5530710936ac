from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core.models import Nota
from core.serializers import NotaSerializer


class NotaViewSet(ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["disciplina__nome", "aluno__nome", "trimestre"]
