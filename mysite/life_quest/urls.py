from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^life_quest/', views.life_quest, name='life_quest'),
    url(r'^calc/', views.calc, name='calc'),
]
