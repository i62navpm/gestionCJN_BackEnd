from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.aspirantes.views import AspiranteViewSet

router = MongoDefaultRouter()
router.register(r'aspirantes', AspiranteViewSet, base_name='aspirantes')

urlpatterns = router.urls
