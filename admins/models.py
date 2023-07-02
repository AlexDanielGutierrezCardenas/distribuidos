from django.db import models

# Create your models here.

class Huesped(models.Model):
	nombres = models.CharField(max_length=50)
	ci = models.CharField(max_length=12, unique=True)
	email = models.EmailField(max_length=100, unique=True)
	fecha_nacimiento = models.DateTimeField()
	telefono = models.IntegerField()
	procedencia = models.CharField(max_length=50)

	def __str__(self):
		return self.nombres

	class Meta:
		ordering = ['nombres']
		verbose_name = 'Huespedes'


class Habitacion(models.Model):
	numero = models.CharField(max_length=2)
	piso = models.CharField(max_length=1)
	tipo = models.CharField(max_length=25, default='Simple')
	precio = models.FloatField()
	estado = models.CharField(max_length=20, default='Libre')

	def __str__(self):
		return f"Piso: { self.piso }, Habitación: { self.numero }"

	class Meta:
		ordering = ['piso', 'numero']
		verbose_name = 'Habitaciones'