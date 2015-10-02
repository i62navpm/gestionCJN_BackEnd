from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.sectores.views import SectorViewSet

router = MongoDefaultRouter()
router.register(r'sectores', SectorViewSet, base_name='sectores')

urlpatterns = router.urls

