"""gestionCJN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from app.cofrades.urls import router as cofrades
from app.sectores.urls import router as sectores
from app.costaleros.urls import router as costaleros
from app.aspirantes.urls import router as aspirantes
from app.directivos.urls import router as directivos
from app.autoridades.urls import router as autoridades
from app.papeletasSitios.urls import router as papeletasSitios
from app.gastosBancarios.urls import router as gastosBancarios
from app.numerosLoteria.urls import router as numerosLoteria
from app.login.views import vista_login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', vista_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url('^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(cofrades.urls)),
    url(r'^api/', include(sectores.urls)),
    url(r'^api/', include(costaleros.urls)),
    url(r'^api/', include(aspirantes.urls)),
    url(r'^api/', include(directivos.urls)),
    url(r'^api/', include(autoridades.urls)),
    url(r'^api/', include(papeletasSitios.urls)),
    url(r'^api/', include(gastosBancarios.urls)),
    url(r'^api/', include(numerosLoteria.urls))
]

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index_app.html)?$', 'serve', kwargs={'path': 'index_app.html'}),
    url(r'^(?P<path>(?:js|css|img|libs|templates)/.*)$', 'serve'),
)