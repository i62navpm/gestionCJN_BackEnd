from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import PapeletaSitioSerializer
from models import PapeletaSitio
from app.cofrades.models import Cofrade
from mongoengine.queryset.visitor import Q


class PapeletaSitioViewSet(ModelViewSet):
    serializer_class = PapeletaSitioSerializer

    def get_queryset(self):
        queryset = PapeletaSitio.objects()

        anios = self.request.query_params.get('anios', None)
        anio = self.request.query_params.get('anio', None)

        if anios:
            return queryset.only("anio").order_by('-anio')
        if anio:
            queryset = queryset.filter(Q(anio=anio))
            for papeletasSitio in queryset:
                for index, value in enumerate(papeletasSitio.papeletas):
                    aux = Cofrade(id=value.cofrade.id,
                                  numeroOrden=value.cofrade.numeroOrden,
                                  datosPersonales={
                                      'nombre': value.cofrade.datosPersonales.nombre + ' ' +
                                                value.cofrade.datosPersonales.apellido1 + ' ' +
                                                value.cofrade.datosPersonales.apellido2})
                    papeletasSitio.papeletas[index].cofrade = aux

        return queryset
