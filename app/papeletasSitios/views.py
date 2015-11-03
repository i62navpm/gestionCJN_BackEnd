from bson import ObjectId
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

    def perform_create(self, serializer):
        queryset = PapeletaSitio.objects(anio=self.request.data['anio'])
        if not queryset:
            serializer.save()
        else:
            self.request.data['papeletas'][0]['cofrade'] = ObjectId(self.request.data['papeletas'][0]['cofrade'])
            if not self.request.data.get('remove', None):
                PapeletaSitio.objects(anio=self.request.data['anio']).update(
                    push__papeletas=self.request.data['papeletas'][0])
            else:
                PapeletaSitio.objects(anio=self.request.data['anio']).update(
                    pull__papeletas=self.request.data['papeletas'][0])
                if not len(PapeletaSitio.objects(anio=self.request.data['anio'])[0].papeletas):
                    PapeletaSitio.objects(anio=self.request.data['anio']).delete()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapeletaSitioViewSet, self).dispatch(*args, **kwargs)
