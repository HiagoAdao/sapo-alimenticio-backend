from django.shortcuts import render
from rest_framework import viewsets
from .models import Alimento, Arquivo
from .serializers import AlimentoSerializer, ArquivoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

from helpers import limpar_arquivos, limpar_tabelas
from extractor import extrair_db


class AlimentosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Alimento.objects.all().order_by('nome')
    serializer_class = AlimentoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class AlimentosProteinasViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.raw("""
        SELECT id, nome, gorduras, quantidade, carboidratos, proteinas, gorduras FROM core_alimento
        GROUP BY id, gorduras, nome, quantidade, carboidratos, proteinas
        HAVING proteinas >= (SELECT AVG(proteinas) FROM core_alimento)
        ORDER BY proteinas DESC """)
    serializer_class = AlimentoSerializer

class AlimentosCarboidratosViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.raw("""
        SELECT id, nome, gorduras, quantidade, carboidratos, proteinas, gorduras FROM core_alimento
        GROUP BY id, gorduras, nome, quantidade, carboidratos, proteinas
        HAVING carboidratos >= (SELECT AVG(carboidratos) FROM core_alimento)
        ORDER BY carboidratos DESC """)
    serializer_class = AlimentoSerializer

class AlimentosGordurasViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.raw("""
        SELECT id, nome, gorduras, quantidade, carboidratos, proteinas, gorduras FROM core_alimento
        GROUP BY id, gorduras, nome, quantidade, carboidratos, proteinas
        HAVING gorduras >= (SELECT AVG(gorduras) FROM core_alimento)
        ORDER BY gorduras DESC """)
    serializer_class = AlimentoSerializer    


class ArquivosViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all().order_by('titulo')
    serializer_class = ArquivoSerializer
    # permission_classes = [permissions.IsAuthenticated]    
    
    @action(methods=['delete'], detail=False)
    def delete(self, request, pk=None):
        limpar_tabelas()
        limpar_arquivos()
        return Response(status=200,data='Limpeza efetuada')

    @action(methods=['put'], detail=False)
    def put(self, request, pk=None):
        extrair_db()
        return Response(status=200,data='Atualização efetuada')        

