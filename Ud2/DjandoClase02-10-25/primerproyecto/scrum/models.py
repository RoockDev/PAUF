from email.policy import default

from django.db import models
from django.db.models import DateField
from datetime import  datetime
from django.utils import timezone


# Create your models here.
class Programador(models.Model):
    TECNOLOGIAS = [('P','PYTHON'),('J','JAVA'),('PHP','PHP')]
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    tecnologia = models.CharField(choices=TECNOLOGIAS, default='P')


    def __str__(self):
        return f"{self.id}, {self.nombre},{self.apellidos}"






class Tarea(models.Model):
    nombreTarea = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    estimacion = models.IntegerField(null=True,blank=True)
    asignada = models.BooleanField(default=False)
    usuario = models.ManyToManyField(Programador)
    fecha_nacimiento = models.DateField(null=True,blank=True)

class Sprint(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.CharField()


    def __str__(self):
        return f"{self.id},{self.nombreTarea},{self.descripcion},{self.estimacion},{self.asignada}"