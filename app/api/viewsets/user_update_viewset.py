from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from ..serializers import UserSerializer


class UserUpdateViewSet(ModelViewSet):
    http_method_names = ['patch']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
