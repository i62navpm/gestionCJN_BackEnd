from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import GastoBancarioSerializer
from models import GastoBancario


class GastoBancarioViewSet(ModelViewSet):
    serializer_class = GastoBancarioSerializer
    queryset = GastoBancario.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GastoBancarioViewSet, self).dispatch(*args, **kwargs)