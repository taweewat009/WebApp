from django.contrib import admin
from django.urls import path , include
from .views import index,blogdetail

urlpatterns = [
    path('',index,name="index"),
    path('blog/<int:id>',blogdetail,name="blogdetail")
]
