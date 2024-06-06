from django import forms
from django.core.exceptions import ValidationError

from .models import Docente

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'})) 
    apellido = forms.CharField(label="Apellido", required=True) 
    dni = forms.IntegerField(label="DNI", required=True)

    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    field = forms.ChoiceField(choices=CHOICES)

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        
        if nombre == "Carlos" and apellido == "Lopez":
            raise ValidationError("El usuario Carlos Lopez ya existe")
        
        if self.cleaned_data["dni"] < 1000000:
            raise ValidationError("El dni debe tener 8 digitos")

        return self.cleaned_data
    

class AltaDocenteModelForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

        error_messages = {
            'dni': {
                'required': 'El campo DNI es Obligatorio ☺'
            }
        }

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]

