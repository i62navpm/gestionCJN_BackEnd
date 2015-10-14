from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import CostaleroSerializer
from models import Costalero


class CostaleroViewSet(ModelViewSet):
    serializer_class = CostaleroSerializer
    queryset = Costalero.objects()
