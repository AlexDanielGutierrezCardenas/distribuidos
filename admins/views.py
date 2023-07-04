from django.shortcuts import render,redirect
from .models import Huesped,Habitacion

def index(request):
    return render(request,'index.html')

def huesped(request):
    huespedes = Huesped.objects.all()
    return render(request,'huespedes/index.html', {'huespedes':huespedes})

def habitacion(request):
    habitaciones = Habitacion.objects.all()
    habita = Habitacion.objects.filter(estado='libre')
    return render(request,'habitaciones/index.html', {'habitaciones':habitaciones,'habita':habita})

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


def eliminarHuesped(request,id):
    huesped=Huesped.objects.get(pk=id)
    huesped.delete()
    return redirect('huespedes_index')

def editar(request, id):
    huesped=Huesped.objects.get(pk=id)
    # return HttpResponse(persona)
    return render(request,'huespedes/editar.html',{'huesped':huesped})

def update_huesped(request,id):
    datos=request.POST
    huesped=Huesped.objects.get(pk=id)
    huesped.nombres=datos.get('nombres')
    huesped.ci=datos.get('ci')
    huesped.correo=datos.get('correo')
    huesped.telefono=datos.get('telefono')
    huesped.procedencia=datos.get('procedencia')
    huesped.save()
    return redirect('huespedes_index')

def eliminarHabitacion(request,id):
    habitacion=Habitacion.objects.get(pk=id)
    habitacion.delete()
    return redirect('habitaciones_index')   

def editarHabitacion(request, id):
    habitacion=Habitacion.objects.get(pk=id)
    # return HttpResponse(persona)
    return render(request,'habitaciones/editar.html',{'habitacion':habitacion})

def update_habitacion(request,id):
    datos=request.POST
    habitacion=Habitacion.objects.get(pk=id)
    habitacion.numero=datos.get('numero')
    habitacion.piso=datos.get('piso')
    habitacion.tipo=datos.get('tipo')
    habitacion.precio=datos.get('precio')
    habitacion.estado=datos.get('estado')
    habitacion.save()
    return redirect('habitaciones_index')