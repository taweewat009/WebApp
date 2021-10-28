from django.contrib import admin
from django.urls import path 
from .views import certificate


urlpatterns = [
    path('',certificate, name="certificate"),
]