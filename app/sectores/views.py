from bson import ObjectId
from rest_framework import status
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from mongoengine.queryset.visitor import Q
from serializers import SectorSerializer
from models import Sector


class SectorViewSet(ModelViewSet):
    serializer_class = SectorSerializer

    def get_queryset(self):
        queryset = Sector.objects()

        calle = self.request.query_params.get('calle', None)
        sector = self.request.query_params.get('sector', None)
        if calle:
            queryset = queryset.filter(Q(calles__iexact=calle))
            return queryset.only("numeroSector")
        if sector:
            queryset = queryset.filter(Q(numeroSector=sector))

        return queryset

    def retrieve(self, request, id=None, **kwargs):
        queryset = Sector.objects(id=id)
        serializer = SectorSerializer(queryset[0])
        return Response([serializer.data])

