
from django.urls import path, include
from .views import index, my_logout,cadastrar_usuario, logar_usuario

urlpatterns = [
    path('', index, name="index"),
    path('logout/', my_logout, name="logout"),
    path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/', logar_usuario, name="logar_usuario"),
]