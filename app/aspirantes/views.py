from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import AspiranteSerializer
from models import Aspirante


class AspiranteViewSet(ModelViewSet):
    serializer_class = AspiranteSerializer
    queryset = Aspirante.objects()
