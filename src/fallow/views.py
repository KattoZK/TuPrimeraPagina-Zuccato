from django.shortcuts import render, redirect
from .models import Conductor, Ganancia, Gasto
from .forms import ConductorForm, MedioForm, GananciaForm, GastoForm

def agregar_conductor(request):
    if request.method == "POST":
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_conductor")
        else:
            form = ConductorForm()
        return render(request, "agregar_conductor.html", {"form": form})

def listar_gastos(request):
    conductores = Conductor.objects.all()
    conductor_seleccionado = request.GET.get("conductor")
    if conductor_seleccionado:
        gastos = Gasto.objects.filter(conductor__id=conductor_seleccionado)
        ganancias = Ganancia.objects.filter(conductor__id=conductor_seleccionado)
        total_ganancias = sum(g.monto for g in ganancias)
        total_gastos = sum(g.monto for g in gastos)
        neto = total_ganancias - total_gastos
    else:
        gastos = Gasto.objects.all()
        neto = None
        return render(request, "listar_gastos.html", {"conductores":conductores, "gastos":gastos, "neto":neto})
    
def total_dia(request):
    conductores = Conductor.objects.all()
    fecha_seleccionada = request.GET.get("fecha")
    conductor_seleccionado = request.GET.get("conductor")
    if fecha_seleccionada and conductor_seleccionado:
        ganancias = Ganancia.objects.filter(conductor__id=conductor_seleccionado, ffecha=fecha_seleccionada)
        gastos = Gasto.objects.filter(conductor__id=conductor_seleccionado, ffecha=fecha_seleccionada)
        total = sum(g.monto for g in ganancias) - sum(g.monto for g in gastos)
    else:
        total = None
        return render(request, "total_dia.html", {"conductores":conductores, "total":total})
    