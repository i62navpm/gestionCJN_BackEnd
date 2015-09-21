from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from mongoengine.queryset.visitor import Q
from serializers import CofradeSerializer
from models import Cofrade

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

    def get_queryset(self):
        queryset = Cofrade.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        numeroOrden = self.request.query_params.get('numeroOrden', None)
        numeroCofrade = self.request.query_params.get('numeroCofrade', None)

        if nombre:
            for term in nombre.split():
                queryset = queryset.filter(Q(datosPersonales__nombre__icontains=term) |
                                           Q(datosPersonales__apellido1__icontains=term) |
                                           Q(datosPersonales__apellido2__icontains=term))

        elif numeroOrden:
            queryset = queryset.filter(Q(numeroOrden=numeroOrden))

        elif numeroCofrade:
            queryset = queryset.filter(Q(numeroCofrade=numeroCofrade))

        return queryset.only('numeroOrden',
                             'numeroCofrade',
                             'datosPersonales.nombre',
                             'datosPersonales.apellido1',
                             'datosPersonales.apellido2',
                             'baja')

    """
    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    """