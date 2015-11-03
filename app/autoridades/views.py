from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import AutoridadSerializer
from models import Autoridad


class AutoridadViewSet(ModelViewSet):
    serializer_class = AutoridadSerializer
    queryset = Autoridad.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutoridadViewSet, self).dispatch(*args, **kwargs)