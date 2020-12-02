from django.shortcuts import render
from reserva.utils import deco, deco2, codificador
from .form import PostForm
from .models import Reserva
from django.utils import timezone
from datetime import datetime
import json

def home(request):
    return render(request, 'home.html', context={})


def decode(request):
    #data2 = deco() #Alternativa para decodificador online
    data = deco2()
    return render(request, 'decodificacion.html', context={'data': data})


def reservar(request):
    return render(request, 'nueva_reserva.html', context={})


def informar(request):
    return render(request, 'info.html', context={})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            exists = Reserva.objects.filter(
                apellido=nuevo.apellido,
                nombre=nuevo.nombre,
                DNI=nuevo.DNI,
                email=nuevo.email,
                fecha=nuevo.fecha).exists()
            if exists:
                return render(request, 'repetida.html', context={})
            elif datetime.strftime(nuevo.fecha, '%Y-%m-%d') < timezone.localtime(timezone.now()).date().isoformat():
                return render(request, 'error_fecha.html', context={})
            else:
                nueva_reserva = form.save(commit=False)
                nueva_reserva.save()
                reserva = Reserva.objects.filter(fecha=nueva_reserva.fecha, email=nueva_reserva.email).first()
                data = {
                    'nombre': nueva_reserva.nombre,
                    'apellido': nueva_reserva.apellido,
                    'DNI': nueva_reserva.DNI,
                    'fecha': str(nueva_reserva.fecha),
                    'email': nueva_reserva.email,
                }
                codificador(data, reserva)
                data['imagen'] = reserva.codigo
                reserva.save()
                return render(request, 'reserva_exitosa.html', context={'data': data})
        else:
            return render(request, "home.html", context={})
