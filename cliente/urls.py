from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('agregar', views.agregar),
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    path('borrar', views.borrar),
]