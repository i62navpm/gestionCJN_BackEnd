from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import DirectivoSerializer
from models import Directivo


class DirectivoViewSet(ModelViewSet):
    serializer_class = DirectivoSerializer
    queryset = Directivo.objects()
