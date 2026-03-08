from django.urls import path
from . import views

# Define as rotas específicas do aplicativo de sorteio
urlpatterns = [
    # Liga a URL vazia à função que executa o sorteio na tela
    path('', views.sorteador_view, name='sorteador'),
]