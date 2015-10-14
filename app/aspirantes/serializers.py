from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Aspirante


class AspiranteSerializer(DocumentSerializer):
    class Meta:
        model = Aspirante