from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import CostaleroSerializer
from models import Costalero


class CostaleroViewSet(ModelViewSet):
    serializer_class = CostaleroSerializer
    queryset = Costalero.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CostaleroViewSet, self).dispatch(*args, **kwargs)
