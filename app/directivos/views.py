from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import DirectivoSerializer
from models import Directivo


class DirectivoViewSet(ModelViewSet):
    serializer_class = DirectivoSerializer
    queryset = Directivo.objects()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DirectivoViewSet, self).dispatch(*args, **kwargs)
