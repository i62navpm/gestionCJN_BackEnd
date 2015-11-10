from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mongoengine.django.auth import User
from rest_framework_mongoengine.viewsets import ModelViewSet
from serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects(id=self.request.user.id).only('username')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)