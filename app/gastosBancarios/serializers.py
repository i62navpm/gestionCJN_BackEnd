from rest_framework_mongoengine.serializers import DocumentSerializer
from models import GastoBancario


class GastoBancarioSerializer(DocumentSerializer):
    class Meta:
        model = GastoBancario