from django.db import models

class Conductor(models.Model): #Clase para registrar conductores
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Medio(models.Model): #Clase para registar por donde se realizo el viaje
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ganancia(models.Model): #Clase para registrar cada ingreso en positivo
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    medio = models.ForeignKey(Medio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.conductor} - {self.monto}"
    
class Gasto(models.Model): #Clase para registrar egresos
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.conductor} - {self.monto}"