from django.shortcuts import render
from .models import Reserva

def index_reserva(request):
    return render(request,'reservas/index_reserva.html')

def nueva_reserva(request):
    return render(request,'reservas/nueva_reserva.html')
