from django.contrib import admin
from django.urls import path, include

# Define as rotas principais do sistema
urlpatterns = [
    # Rota para a interface de administração do Django
    path('admin/', admin.site.urls),
    
    # Encaminha o acesso da página inicial para o aplicativo 'sorteador'
    path('', include('sorteador.urls')),
]