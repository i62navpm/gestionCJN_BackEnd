from django.http import HttpResponse
from django.views.generic import View
from app.cofrades.models import Cofrade
from mongogeneric.list import ListView
from mongogeneric.detail import DetailView

class Prueba(View):
    def get(self, request):
        # <la logica de la vista>
        cof = Cofrade.objects.first()
        print cof
        return HttpResponse('prueba')

class Prueba2(ListView):
    queryset = Cofrade.objects
    template_name = 'cofrade_list.html'

class Prueba3(DetailView):
    queryset = Cofrade.objects
    template_name = 'cofrade_detail.html'