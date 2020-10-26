from django.db import models

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField(auto_now_add=True)
