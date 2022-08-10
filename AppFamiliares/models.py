from django.db import models


class Familiar(models.Model):
    relacion= models.CharField(max_length=30)
    nombre= models.CharField(max_length= 40)
    apellido= models.CharField(max_length= 40)
    fecha_nacimiento= models.DateField()
    cedula= models.IntegerField()

# Create your models here.
