from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('reserva_index',views.index_reserva,name='reserva_index'),
    path('reserva_nueva',views.nueva_reserva,name='nueva_reserva'),
    path('updateEstado/<int:id>/<int:id_habitacion>',views.updateEstado,name='updateEstado'),
    path('editarReserva/<int:id>',views.editar,name='editarReserva'),
    path('update/reserva/<int:id>/<int:id_huesped>/<int:id_habitacion>',views.updateReserva,name='update_reserva'),
]