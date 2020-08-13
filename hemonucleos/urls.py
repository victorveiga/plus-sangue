from django.contrib import admin
from django.urls import path

from .views import store, create, update

urlpatterns = [
    path('', store, name='hemonucleos'),
    path('novo/', create, name='create_hemonucleo'),
    path('hemonucleo/<int:id>', update, name='update_hemonucleo'),
]
