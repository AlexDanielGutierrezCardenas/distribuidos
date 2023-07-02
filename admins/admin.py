from django.contrib import admin
from .models import Huesped, Habitacion

# Register your models here.

admin.site.register([Huesped, Habitacion])