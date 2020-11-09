from rest_framework import serializers
from .models import Alimento, Arquivo

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = ['id', 'nome', 'quantidade', 'proteinas','carboidratos','gorduras']


class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = ['id', 'titulo', 'caminho']