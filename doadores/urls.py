from django.contrib import admin
from django.urls import path

from .views import store, create, update

urlpatterns = [
    path('', store, name='doadores'),
    path('novo/', create, name='create_doador'),
    path('doador/<int:id>', update, name='update_doador'),
]
