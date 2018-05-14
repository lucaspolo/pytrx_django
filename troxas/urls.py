from django.urls import path
from .views import troxa_listar

urlpatterns = [
    path('listar/', troxa_listar, name='troxa_listar')
]
