from django.urls import path
from .views import buscar_endereco

urlpatterns = [
    path('', buscar_endereco, name='home'),  # Adiciona a URL raiz
    path('buscar-cep/', buscar_endereco, name = 'buscar_o_endereco' )
]