from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core.models import Turma
from core.serializers import TurmaSerializer
from core.serializers.turma import TurmaListSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["curso__disciplina__id"]

    def get_serializer_class(self):
        if self.action == "list":
            return TurmaListSerializer
        elif self.action == "retrieve":
            return TurmaSerializer
