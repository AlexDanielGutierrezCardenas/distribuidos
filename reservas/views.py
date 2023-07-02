from django.shortcuts import render
from .models import Reserva

def index_reserva(request):
    reservas = Reserva.objects.all()
    return render(request,'reservas/index.html', {'reservas':reservas})

def nueva_reserva(request):
    return render(request,'reservas/nueva_reserva.html')
