from django.shortcuts import render
from reserva.utils import decodificar_2, codificador
from .form import PostForm
from .models import Reserva
from django.utils import timezone
from datetime import datetime


def home(request):
    return render(request, 'home.html', context={})


def decodificar(request):
    # data = decodificar_1() #Alternativa para decodificador online externo
    data = decodificar_2()
    return render(request, 'decodificacion.html', context={'data': data})


def reservar(request):
    return render(request, 'nueva_reserva.html', context={})


def informar(request):
    return render(request, 'info.html', context={})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            nueva_reserva = form.save(commit=False)
            exists = Reserva.objects.filter(
                apellido=nueva_reserva.apellido,
                nombre=nueva_reserva.nombre,
                DNI=nueva_reserva.DNI,
                email=nueva_reserva.email,
                fecha=nueva_reserva.fecha).exists()
            if exists:
                return render(request, 'repetida.html', context={})
            elif datetime.strftime(nueva_reserva.fecha, '%Y-%m-%d') < timezone.localtime(timezone.now()).date().isoformat():
                return render(request, 'error_fecha.html', context={})
            else:
                nueva_reserva.save()
                reserva = Reserva.objects.get(
                    fecha=nueva_reserva.fecha,
                    email=nueva_reserva.email,
                    nombre=nueva_reserva.nombre,
                    apellido=nueva_reserva.apellido,
                    DNI=nueva_reserva.DNI,
                    hora=nueva_reserva.hora)
                data = {
                    'nombre': reserva.nombre,
                    'apellido': reserva.apellido,
                    'DNI': reserva.DNI,
                    'fecha': str(reserva.fecha),
                    'hora': str(reserva.hora),
                    'email': reserva.email,
                }
                codificador(data, reserva)
                data['imagen'] = reserva.codigo
                reserva.save()
                return render(request, 'reserva_exitosa.html', context={'data': data})
    return render(request, "home.html", context={})
