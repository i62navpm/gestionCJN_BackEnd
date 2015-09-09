from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Cofrade


class CofradeSerializer(DocumentSerializer):
    class Meta:
        model = Cofrade