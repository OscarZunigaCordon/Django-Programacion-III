from django.db import models

# Create your models here.


class Estudiantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=8)


class Asignacion(models.Model):
    codigo = models.CharField(max_length=10)


class Clases(models.Model):
    nombre = models.CharField(max_length=30)
    nota = models.IntegerField()
    estado = models.BooleanField()

class Maestros(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
