from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name='base'),
    path('criar/',views.criar, name='criar'),
    path('index/', views.index, name='index'),
    path('consultar/', views.consultar, name='consultar'),
    path('atualizar/<int:id>',views.atualizar, name='atualizar_id'),
    path('atualizar/',views.atualizar, name='atualizar'),
    path('deletar/<int:id>',views.deletar, name='deletar_id'),
    path('deletar/',views.deletar, name='deletar'),
]
