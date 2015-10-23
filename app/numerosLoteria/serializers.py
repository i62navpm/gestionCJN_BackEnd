from rest_framework_mongoengine.serializers import DocumentSerializer
from models import NumerosLoteria


class NumerosLoteriaSerializer(DocumentSerializer):
    class Meta:
        model = NumerosLoteria