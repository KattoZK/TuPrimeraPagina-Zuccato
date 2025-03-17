from django import forms
from .models import Conductor, Medio, Ganancia, Gasto

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ["Nombre"]

class MedioForm(forms.ModelForm):
    class Meta:
        model = Medio
        fields = ["Nombre"]

class GananciaForm(forms.ModelForm):
    class Meta:
        model = Ganancia
        fields = ["conductor", "medio", "monto"]

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ["conductor","descripcion","monto"]