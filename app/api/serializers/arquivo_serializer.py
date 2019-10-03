from rest_framework.serializers import ModelSerializer
from ...models import Arquivo


class ArquivoSerializer(ModelSerializer):
    class Meta:
        model = Arquivo
        fields = ('id', 'titulo', 'arquivo')