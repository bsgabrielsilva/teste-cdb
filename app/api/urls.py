from rest_framework import routers

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .viewsets import *


router = routers.DefaultRouter()
router.register(r'arquivo', ArquivoViewSet, basename='arquivo')
router.register(r'registrar', UserRegisterViewSet, basename='registrar')
router.register(r'atualizar', UserUpdateViewSet, basename='atualizar')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
]