from django.http import HttpResponse
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from mongoengine.queryset.visitor import Q
from serializers import CofradeSerializer
from models import Cofrade
from paginationClass import StandardResultsSetPagination
import json

# from django.http import HttpResponse
# from django.views.generic import View
# from app.cofrades.models import Cofrade
# from mongogeneric.list import ListView
# from mongogeneric.detail import DetailView
#
# class Prueba(View):
#     def get(self, request):
#         # <la logica de la vista>
#         cof = Cofrade.objects.first()
#         print cof
#         return HttpResponse('prueba')
#
# class Prueba2(ListView):
#     queryset = Cofrade.objects
#     template_name = 'cofrade_list.html'
#
# class Prueba3(DetailView):
#     queryset = Cofrade.objects
#     template_name = 'cofrade_detail.html'

class CofradeViewSet(ModelViewSet):
    serializer_class = CofradeSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Cofrade.objects(baja__exists='Bajas' in self.request.path)

        nombre = self.request.query_params.get('nombre', None)
        numeroOrden = self.request.query_params.get('numeroOrden', None)
        numeroCofrade = self.request.query_params.get('numeroCofrade', None)

        if nombre:
            for term in nombre.split():
                queryset = queryset.filter(Q(datosPersonales__nombre__icontains=term) |
                                           Q(datosPersonales__apellido1__icontains=term) |
                                           Q(datosPersonales__apellido2__icontains=term)).order_by('numeroOrden')

        elif numeroOrden:
            queryset = queryset.filter(Q(numeroOrden=numeroOrden)).order_by('numeroOrden')

        elif numeroCofrade:
            queryset = queryset.filter(Q(numeroCofrade=numeroCofrade)).order_by('numeroOrden')

        return queryset.only('numeroOrden',
                             'datosPersonales.nombre',
                             'datosPersonales.apellido1',
                             'datosPersonales.apellido2',
                             'datosPersonales.direccion.calle',
                             'datosPersonales.direccion.municipio',
                             'datosPersonales.direccion.provincia',
                             'baja').order_by('numeroOrden')

    def retrieve(self, request, id=None, **kwargs):
        queryset = Cofrade.objects(id=id)
        serializer = CofradeSerializer(queryset[0])
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
        if serializer.context['request'].GET.get('updateNumeroCofrade', None):
            numeroCofrade = 1
            for cofrade in Cofrade.objects(baja__exists=False).order_by('numeroOrden'):
                cofrade.numeroCofrade = numeroCofrade
                numeroCofrade += 1
                cofrade.save()
    """
    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    """


def calles(request):
    calleParam = request.GET.get('calle', None)

    calles = Cofrade.objects.distinct("datosPersonales.direccion.calle")
    if calleParam:
        calles = [aux for aux in calles if calleParam.lower() in aux.lower()]
    direcciones = []
    for calle in calles:
        direccion = {}
        cofrade = Cofrade.objects(datosPersonales__direccion__calle__iexact=calle)[0]
        direccion['calle'] = calle
        direccion['municipio'] = cofrade.datosPersonales.direccion.municipio
        direccion['cp'] = cofrade.datosPersonales.direccion.cp
        direccion['provincia'] = cofrade.datosPersonales.direccion.provincia
        direcciones.append(direccion)

    return HttpResponse(json.dumps(direcciones), content_type="application/json")

def registros(request):
    registro = {'numeroOrden': Cofrade.objects.order_by('-numeroOrden')[0]['numeroOrden'] + 1,
                'numeroCofrade': Cofrade.objects.order_by('-numeroCofrade')[0]['numeroCofrade'] + 1}

    return HttpResponse(json.dumps(registro), content_type="application/json")



