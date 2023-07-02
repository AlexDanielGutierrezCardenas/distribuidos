from django.shortcuts import render,redirect
from .models import Huesped,Habitacion

def index(request):
    return render(request,'index.html')

def huesped(request):
    huespedes = Huesped.objects.all()
    return render(request,'huespedes/index.html', {'huespedes':huespedes})

def habitacion(request):
    habitaciones = Habitacion.objects.all()
    return render(request,'habitaciones/index.html', {'habitaciones':habitaciones})

def nuevo_habitacion(request):
    if request.method == 'GET':
        return render(request,'habitaciones/nuevo_habitacion.html')
    else:
        data = request.POST
        habitacion = Habitacion(
            numero=data.get('numero'),
            piso=data.get('piso'),
            tipo=data.get('tipo'),
            precio=data.get('precio'),
            estado=data.get('estado')
        )
        habitacion.save()
        return redirect('habitaciones_index')

def nuevo_huesped(request):
    if request.method == 'GET':
        return render(request,'huespedes/nuevo_huesped.html')
    else:
        data = request.POST
        huesped = Huesped(
            nombres=data.get('nombres'),
            ci=data.get('ci'),
            email=data.get('email'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            telefono=data.get('telefono'),
            procedencia=data.get('procedencia')
        )
        huesped.save()
    return redirect('huespedes_index')
# Create your views here.
