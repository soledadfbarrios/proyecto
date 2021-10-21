from django.contrib import admin

# Register your models here.

from .models import Autor, Libro
#importamos el modelo Autor

admin.site.register(Autor) 
#registramo la clase creada

admin.site.register(Libro) 