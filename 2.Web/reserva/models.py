from django.db import models


class Reserva(models.Model):
    codigo = models.ImageField(upload_to='')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    DNI = models.IntegerField()
    fecha = models.DateField()
    email = models.EmailField(max_length=254)
