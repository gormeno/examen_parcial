from tkinter import commondialog
from django.db import models
import datetime

# Create your models here.
class usuarios_app(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo = models.CharField(max_length=128,default='')
    contrasena = models.CharField(max_length=128,default='')

class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fecha_cracion = models.DateField(default=datetime.date.today)
    fecha_entrega = models.DateField(default=datetime.date.today)
    responsable = models.CharField(max_length=128,default='')
    estado = models.CharField(max_length=128,default='PROGRESO')