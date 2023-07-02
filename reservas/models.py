from django.db import models
from admins.models import Habitacion, Huesped

# Create your models here.

class Reserva(models.Model):
	fecha = models.DateTimeField()
	duracion = models.IntegerField()
	estado = models.CharField(max_length=10, default='Activo')

	huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE)
	habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

	def __str__(self):
		return f"{ self.huesped } { self.habitacion }"

	class Meta:
		ordering = ['estado', 'fecha']
