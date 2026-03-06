from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorteador_view, name='sorteador'),
]