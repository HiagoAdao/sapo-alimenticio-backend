from django.db import models, signals
from extractor import extrair_db
# from django.utils import timezone
from datetime import datetime

class Alimento(models.Model):
    nome = models.CharField(unique=True, max_length=70)
    quantidade = models.IntegerField()
    proteinas = models.IntegerField()
    carboidratos = models.IntegerField()
    gorduras = models.IntegerField()
    criado_em = models.DateTimeField(editable=False, null=True)
    atualizado_em = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.criado_em:
            self.criado_em = datetime.now()
        self.atualizado_em = datetime.now()
        return super(Alimento, self).save(*args, **kwargs)    

    def __str__(self):
        return self.nome

class Arquivo(models.Model):
    titulo = models.CharField(unique=True, max_length=70)
    caminho = models.FileField(upload_to='filestxt', max_length=100, blank=True)

    criado_em = models.DateTimeField(editable=False, null=True)
    atualizado_em = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.criado_em:
            self.criado_em = datetime.now()
        self.atualizado_em = datetime.now()
        extrair_db()

        return super(Arquivo, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo