from django.contrib import admin
from django.urls import path

from .views import helloworld

urlpatterns = [
    path('home/', helloworld, name='doadores')
]
