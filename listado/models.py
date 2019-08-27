from django.db import models


# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=200) #campo cadena de caracteres
    horario = models.CharField(max_length=200)
    clasificacion = models.CharField (max_length=200)
    

    created = models.DateField( auto_now_add=True) #campo de Fecha y hora se ejecuta solo al crearse, añadira hora solo al crearse
    updated = models.DateField(auto_now=True) #campo de Fecha y hora se actualiza cuando se modifica


 #def __str__(self):
#return self.title