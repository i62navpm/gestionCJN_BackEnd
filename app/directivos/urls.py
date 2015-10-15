from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.directivos.views import DirectivoViewSet

router = MongoDefaultRouter()
router.register(r'directivos', DirectivoViewSet, base_name='directivos')

urlpatterns = router.urls
