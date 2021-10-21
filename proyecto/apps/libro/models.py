from django.db import models
from django.db.models.base import Model

# Create your models here.

class Autor(models.Model): #lo toma como tabla para luego poder migrar como una base de datos
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200, blank=False, null=False)
    #maximo de 200, que no quede en blanco y null
    apellido = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=True, auto_now_add=False)
    #se agrega automaticamente la fecha con auto_now
    #textefields sin limitación de catacteres

    class Meta:
    #datos de los nombres que va recibir esos datos
      verbose_name='Autortito'
      verbose_name_plural = 'Autores'
      #configuración de vista (meta) es para inicar la forma que voy a mostrar los datos
      ordering= ['apellido']


#se crea una isntancia de ese objeto para que muestre con las siguiente descripción, en este caso NOMBRE
    def __str__(self):
        return self.apellido


#--------------#-------------------
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null =False)
    fecha_publicacion =models.DateField('Fecha de publicacion', blank=False, null=False)
    #cuando la relación es de uno a uno
    #autor_id = models.OneToOneField(Autor, on_delete= models.CASCADE) #asigno a la tabla que hago referencia, borro la asignacion
    #relacion de uno a muchos
    #autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)
       #muchos a muchos
    autor_id = models.ManyToManyField(Autor)
    
    class Meta:
        verbose_name='Librito'
        verbose_name_plural = 'Libros'
        ordering= ['fecha_publicacion']

    def __str__(self):
        return self.fecha_publicacion