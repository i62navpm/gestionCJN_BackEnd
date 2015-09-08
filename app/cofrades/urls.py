from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', Prueba2.as_view(), name='lista-cofrades'),
    url(r'^(?P<pk>[a-z0-9]{24})/$', Prueba3.as_view(), name='detalle-cofrade'),
]