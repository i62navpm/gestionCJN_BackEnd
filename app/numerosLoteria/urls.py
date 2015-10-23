from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.numerosLoteria.views import NumerosLoteriaViewSet

router = MongoDefaultRouter()
router.register(r'numerosLoteria', NumerosLoteriaViewSet, base_name='numerosLoteria')

urlpatterns = router.urls
