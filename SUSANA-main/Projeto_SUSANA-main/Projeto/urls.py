"""Projeto_SAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.models import models
from app.views import index, home, edit_profile
from app.views import  Equipe
from django.urls import include, path
from app import views

urlpatterns = [
    path('', index, name='index'),
    path('home', home),
    path('registro/', include('customauth.urls')), 
    path('edit_profile/<int:pk>/', edit_profile, name='url_edit_profile'),
    path('Equipe - SAS/', Equipe, name="url_equipe"),
    #urls bot e gráfico
    path('grafico/', views.graficoHipertensaoDiabetes, name="grafico"),
    path('grafico-hipertensao/', views.graficoHipertensao, name="grafico-hipertensao"),
    path('grafico-diabetes-t1/', views.graficoDiabetesTipo1, name="grafico-diabetes-t1"),
    path('grafico-diabetes-t2/', views.graficoDiabetesTipo2, name="grafico-diabetes-t2"),
    path("bot/<int:v1>/<int:v2>", views.bot, name = "bot"),
    path("selecionar/", views.seleciona, name = "selecionar"),
    path("escolha-grafico/", views.escolhaGrafico, name = "escolha-grafico"),
]
