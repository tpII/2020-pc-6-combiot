from django.db import models
from django.contrib.auth.models import User
from turno.models import Turno


class Reserva(models.Model):
    codigo = models.ImageField(upload_to='usuario/imagenes')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
