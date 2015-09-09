from models import Cofrade
from serializers import CofradeSerializer
from rest_framework_mongoengine.viewsets import ModelViewSet

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
    queryset = Cofrade.objects.all()
    serializer_class = CofradeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)