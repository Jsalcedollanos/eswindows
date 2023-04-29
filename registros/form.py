from django import forms
from django.core import validators
from registros.models import *

class FormCliente(forms.Form):

    identificacion = forms.CharField(
        label = "Identificacion",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu identificacion',
            'class': 'txt-ide'
            }
        ),
        validators=[
            
            validators.MinLengthValidator(8, 'Identificacion demasiado corta'),
            validators.MaxLengthValidator(12, 'Identificacion demasiado larga')
        ]
    )

    nombre = forms.CharField(
        label = "Nombre",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu nombre',
            'class': 'txt-nombre'
            }
        ),
        validators=[
            validators.MinLengthValidator(2, 'El nombre es demasiado corto'),
            validators.MaxLengthValidator(30, 'Nombre es demasiado largo revisa.'),
            validators.RegexValidator(regex='[a-zA-Z]', message='Solo se aceptan letras!')
        ]
    )

    direccion = forms.CharField(
        label = "Direccion",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu direccion',
            'class': 'txt-direccion'
            }
        ),
        validators=[
            validators.MinLengthValidator(10, 'Revisa bien tu direccion'),
            validators.MaxLengthValidator(35, 'Revisa tu direccion, demasiado extensa!')
        ]
    )

    telefono = forms.CharField(
        label = "Telefono",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu telefono',
            'class': 'txt-telefono'
            }
        ),
        validators=[
            validators.MinLengthValidator(10, 'Tu telefono no concuerda'),
            validators.MaxLengthValidator(15, 'Demasiados numeros, revisa tu telefono.')
        ]
    )

    nacionalidad = forms.CharField(
        label = "Nacionalidad",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu nacionalidad',
            'class': 'txt-nacionalidad'
            }
        ),
        validators=[
            validators.MinLengthValidator(3, 'Nacionalidad muy corta revisa primero!'),
            validators.MaxLengthValidator(25, 'Revisa bien tu nacionalidad, demasiado extensa!')
        ]
    )

    correo = forms.EmailField(
        label = "Email",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': 'Ingresa tu correo',
            'class': 'txt-correo'
            }
        ),
        validators=[
            validators.MinLengthValidator(5, 'Correo demasiado corto, Revisa bien!'),
            validators.MaxLengthValidator(50, 'Correo demasiado extenso, revisa bien!'),
            validators.EmailValidator()
        ]
    )


class FormOrden(forms.Form):

   

    detalle = forms.CharField(
        label = "detalle",
        required = True,
        widget = forms.TextInput(
        attrs = {
            'placeholder': '',
            'class': 'txt-detalle'
            }
        ),
        
    )

    

    