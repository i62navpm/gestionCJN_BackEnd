from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Autoridad


class AutoridadSerializer(DocumentSerializer):
    class Meta:
        model = Autoridad