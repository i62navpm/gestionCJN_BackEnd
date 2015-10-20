from rest_framework_mongoengine.serializers import DocumentSerializer
from models import PapeletaSitio


class PapeletaSitioSerializer(DocumentSerializer):
    class Meta:
        model = PapeletaSitio