from django.contrib import admin
from .models import Conductor, Medio, Ganancia, Gasto

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ("nombre", )

@admin.register(Medio)
class MedioAdmin(admin.ModelAdmin):
    list_display = ("nombre", )

@admin.register(Ganancia)
class GananciaAdmin(admin.ModelAdmin):
    list_display = ("conductor", "media", "monto", "fecha")

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ("conductor", "descripcion", "monto", "fecha")



# Register your models here.
