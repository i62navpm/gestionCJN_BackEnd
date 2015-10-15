from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import AutoridadSerializer
from models import Autoridad


class AutoridadViewSet(ModelViewSet):
    serializer_class = AutoridadSerializer
    queryset = Autoridad.objects()
