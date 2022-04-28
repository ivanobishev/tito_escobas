from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    explicacion = models.TextField(max_length=500)
    archivado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre
