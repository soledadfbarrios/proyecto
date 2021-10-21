from django.urls import path
from .views import Home

urlpatterns = [
    path('',Home, name='index' ),
    #recibe 3 parametros, lo que va a escribir el usuario
    #llama a la función Home
    #identificador de nombre url (solo se utiliza con plantillas de Django)
]