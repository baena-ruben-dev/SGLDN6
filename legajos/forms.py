from django import forms
from .models import Docente, Documento, CargoDocente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'tipo_documento', 'numero_documento', 'cuil', 'email', 'telefono', 'fecha_nacimiento', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'cuil': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'tipo', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Título de Grado Lic. en Sistemas'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = CargoDocente
        fields = ['tipo_cargo', 'espacio_curricular', 'horas_catedra', 'condicion', 'turno']
        widgets = {
            'tipo_cargo': forms.Select(attrs={'class': 'form-select'}),
            'espacio_curricular': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_catedra': forms.NumberInput(attrs={'class': 'form-control'}),
            'condicion': forms.Select(attrs={'class': 'form-select'}),
            'turno': forms.Select(attrs={'class': 'form-select'}),
        }