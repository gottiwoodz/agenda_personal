from django.db import models
#create your models here.
from django.db import models

class Cliente (models.Model):
    nombre = models.CharField (max_lenght=100)
    telefono = models.CharField (max_length=20, blanck=True)
    def __str__(self):
        return self.nombre
class Servicio(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.IntegerField()
    duracion_min = models.IntegerField(default=30)
    def __str__(self):
        return self.nombre