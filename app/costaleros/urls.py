from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.costaleros.views import CostaleroViewSet

router = MongoDefaultRouter()
router.register(r'costaleros', CostaleroViewSet, base_name='costaleros')

urlpatterns = router.urls
