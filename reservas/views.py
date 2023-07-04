from django.shortcuts import render,HttpResponse,redirect
from .models import Reserva
from admins.models import Huesped,Habitacion
from datetime import datetime

def index_reserva(request):
    reservas = Reserva.objects.all()
    return render(request,'reservas/index.html', {'reservas':reservas})

def nueva_reserva(request):
    if request.method == 'GET':
        huespedes = Huesped.objects.all()
        habitaciones = Habitacion.objects.all()
        return render(request,'reservas/nueva_reserva.html', {'huespedes':huespedes ,'habitaciones':habitaciones} )
    else:
        data = request.POST
        reserva = Reserva(
            fecha=data.get('fecha'),
            duracion=data.get('duracion'),
            estado=data.get('estado'),
            huesped=Huesped.objects.get(pk=data.get('huesped')),
            habitacion=Habitacion.objects.get(pk=data.get('habitacion')),
        )
        reserva.save()
        if data.get('estado')=='Activo':
            habitacion = Habitacion.objects.get(pk=data.get('habitacion'))
            habitacion.estado="ocupado"
            habitacion.save()

    return redirect('reserva_index')
    
    
def updateEstado(request, id ,id_habitacion):
    update=Reserva.objects.get(pk=id)
    # update.reserva.id
    # return HttpResponse (id_habitacion)
    habitacion = Habitacion.objects.get(pk=id_habitacion)
    habitacion.estado="libre"
    habitacion.save()
    update.estado="Registrado"
    update.save()
    Reserva.objects.create(
        fecha=datetime.now(),
        duracion=update.duracion,
        estado="Inactivo",
        huesped=update.huesped,
        habitacion=update.habitacion,
    )
    return redirect('reserva_index')

def editar(request, id):
    reserva=Reserva.objects.get(pk=id)
    # return HttpResponse(persona)
    return render(request,'reservas/editar.html',{'reserva':reserva})

def updateReserva(request, id ,id_huesped, id_habitacion):
    datos=request.POST
    reserva=Reserva.objects.get(pk=id)
    huesped=Huesped.objects.get(pk=id_huesped)
    habitacion=Habitacion.objects.get(pk=id_habitacion)
    reserva.fecha=datos.get('fecha')
    reserva.duracion=datos.get('duracion')
    reserva.estado=datos.get('estado')
    reserva.huesped=huesped
    reserva.habitacion=habitacion
    reserva.save()
    return redirect('reserva_index')

    
    