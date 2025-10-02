from django.db import models

# Create your models here.
class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.nombre},{self.apellidos}"

class Tarea(models.Model):
    nombreTarea = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    estimacion = models.IntegerField(null=True,blank=True)
    asignada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Programador,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.id},{self.nombreTarea},{self.descripcion},{self.estimacion},{self.asignada}"