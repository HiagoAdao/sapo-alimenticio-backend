from django.contrib import admin
from .models import Alimento, Arquivo

# Register your models here.

admin.site.register(Alimento)
admin.site.register(Arquivo)