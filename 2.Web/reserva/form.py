from django import forms

from .models import Reserva

class PostForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = [
            'nombre',
            'apellido',
            'DNI',
            'fecha',
            'hora',
            'email'
        ]
