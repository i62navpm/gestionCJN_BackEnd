from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import NumerosLoteriaSerializer
from models import NumerosLoteria


class NumerosLoteriaViewSet(ModelViewSet):
    serializer_class = NumerosLoteriaSerializer
    queryset = NumerosLoteria.objects()
