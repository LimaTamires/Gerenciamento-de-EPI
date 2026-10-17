from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='nucleo-inicial'),
    path('colaborador', views.colaborador, name='nucleo-colaborador'),
    path('colaborador/<int:id>/', views.tela_editar, name='nucleo-editar'),
    path('colaborador/salvar/<int:id>/', views.atualizar, name='nucleo-atualizar'),
]