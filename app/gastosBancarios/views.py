from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import GastoBancarioSerializer
from models import GastoBancario


class GastoBancarioViewSet(ModelViewSet):
    serializer_class = GastoBancarioSerializer
    queryset = GastoBancario.objects()
