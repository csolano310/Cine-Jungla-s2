from django.contrib import admin
from django.urls import path
from apps.tiquetes import views

urlpatterns = [
    path('', views.index),
]
