from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import NumerosLoteriaSerializer
from models import NumerosLoteria


class NumerosLoteriaViewSet(ModelViewSet):
    serializer_class = NumerosLoteriaSerializer
    queryset = NumerosLoteria.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NumerosLoteriaViewSet, self).dispatch(*args, **kwargs)
