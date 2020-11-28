from django.shortcuts import render
from reserva.utils import deco, deco2, codificador
from django.views.generic import CreateView
from .form import PostForm
from django.http import HttpResponse
from .models import Reserva


def home(request):
    return render(request, 'home.html', context={})


def decode(request):
    #data = deco()
    data = deco2()
    print(data)
    return render(request, 'decodificacion.html', context={'data': data})


def reservar(request):
    return render(request, 'nueva_reserva.html', context={})


def informar(request):
    return render(request, 'info.html', context={})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Validar fecha futura y no repetida para el dni.
            #validar nombre con dni
            nueva_reserva = form.save(commit=False)
            nueva_reserva.save()
            reserva = Reserva.objects.filter(fecha=nueva_reserva.fecha, email=nueva_reserva.email).first()
            data = {
                'nombre': nueva_reserva.nombre,
                'apellido': nueva_reserva.apellido,
                'DNI': nueva_reserva.DNI,
                'fecha': nueva_reserva.fecha,
                'email': nueva_reserva.email,
            }
            codificador(data, reserva)
            data['imagen'] = reserva.codigo
            reserva.save()
            return render(request, 'reserva_exitosa.html', context={'data': data})
        else:
            return render(request, "home.html", context={})
