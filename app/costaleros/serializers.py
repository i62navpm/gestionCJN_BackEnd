from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Costalero


class CostaleroSerializer(DocumentSerializer):
    class Meta:
        model = Costalero