from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.gastosBancarios.views import GastoBancarioViewSet

router = MongoDefaultRouter()
router.register(r'gastosBancarios', GastoBancarioViewSet, base_name='gastosBancarios')

urlpatterns = router.urls
