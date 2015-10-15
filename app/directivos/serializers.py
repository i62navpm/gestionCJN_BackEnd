from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Directivo


class DirectivoSerializer(DocumentSerializer):
    class Meta:
        model = Directivo