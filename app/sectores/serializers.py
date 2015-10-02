from rest_framework_mongoengine.serializers import DocumentSerializer
from models import Sector


class SectorSerializer(DocumentSerializer):
    class Meta:
        model = Sector