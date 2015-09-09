from rest_framework_mongoengine.routers import MongoDefaultRouter
from app.cofrades.views import CofradeViewSet

router = MongoDefaultRouter()
router.register(r'cofrades', CofradeViewSet, base_name='cofrades')