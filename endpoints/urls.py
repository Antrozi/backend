from django.urls import path
from . import views

urlpatterns=[
    path("login", views.login),
    path("comidas/listar", views.obtenerCategoria)
]