from mongoengine.django.auth import User
from rest_framework_mongoengine.serializers import DocumentSerializer


class UserSerializer(DocumentSerializer):
    class Meta:
        model = User