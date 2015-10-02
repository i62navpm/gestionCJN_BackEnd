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

    def create(self, request, *args, **kwargs):
        request.data['cofrade'] = ObjectId(request.data['cofrade']['id'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, id=None, **kwargs):
        queryset = Sector.objects(id=id)
        serializer = SectorSerializer(queryset[0])
        return Response(serializer.data)

