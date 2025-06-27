from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    # Vista principal - Lista de clientes (la única que necesitamos)
    path('', views.ListaClientes.as_view(), name='lista_clientes'),
]
