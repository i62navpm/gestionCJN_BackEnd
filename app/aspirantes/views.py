from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import AspiranteSerializer
from models import Aspirante


class AspiranteViewSet(ModelViewSet):
    serializer_class = AspiranteSerializer
    queryset = Aspirante.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AspiranteViewSet, self).dispatch(*args, **kwargs)