from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.papeletasSitios.views import PapeletaSitioViewSet

router = MongoDefaultRouter()
router.register(r'papeletasSitios', PapeletaSitioViewSet, base_name='papeletasSitios')

urlpatterns = router.urls
