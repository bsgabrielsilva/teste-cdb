from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..serializers import ArquivoSerializer
from ...models import Arquivo


class ArquivoViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = ArquivoSerializer
    queryset = Arquivo.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]