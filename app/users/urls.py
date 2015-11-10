from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.users.views import UserViewSet

router = MongoDefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = router.urls
