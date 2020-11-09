"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import AlimentosViewSet, ArquivosViewSet, AlimentosProteinasViewSet, AlimentosCarboidratosViewSet, AlimentosGordurasViewSet


router = routers.DefaultRouter()
router.register(r'api/alimentos/proteinas', AlimentosProteinasViewSet)
router.register(r'api/alimentos/carboidratos', AlimentosCarboidratosViewSet)
router.register(r'api/alimentos/gorduras', AlimentosGordurasViewSet)
router.register(r'api/alimentos', AlimentosViewSet)
router.register(r'api/arquivos', ArquivosViewSet)
# router.register(r'api/arquivos/limpar', ArquivosLimparViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
