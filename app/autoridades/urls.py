from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.autoridades.views import AutoridadViewSet

router = MongoDefaultRouter()
router.register(r'autoridades', AutoridadViewSet, base_name='autoridades')

urlpatterns = router.urls
