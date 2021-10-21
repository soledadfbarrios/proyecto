from django import forms 
#importar forms

from .models import Autor
#propio sistema de plantillas
#creamos una clase por cada modelo

class AutorForm(forms.ModelForm):

    class Meta:
        #hace referencia a los metadatos que utilizara el formulario
        #en esta clase vamos a declarar una variable Autor, que viene del modelo
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']