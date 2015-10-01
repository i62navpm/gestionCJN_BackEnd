from django.conf.urls import url
from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.cofrades.views import CofradeViewSet, calles, registros

router = MongoDefaultRouter()
router.register(r'cofrades', CofradeViewSet, base_name='cofrades')
router.register(r'cofradesBajas', CofradeViewSet, base_name='cofrades')

urlpatterns = router.urls

urlpatterns += [
    url(r'calles/', calles),
    url(r'registros/', registros)
]
