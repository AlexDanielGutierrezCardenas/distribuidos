from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('huesped',views.huesped,name='huespedes_index'),
    path('habitacion',views.habitacion,name='habitaciones_index'),
    path('nuevo/habitacion',views.nuevo_habitacion,name='nuevo_habitacion'),
    path('nuevo/huesped',views.nuevo_huesped,name='nuevo_huesped'),
    path('eliminar/huesped/<int:id>',views.eliminarHuesped,name='eliminar_huesped'),
    path('editar/huesped/<int:id>',views.editar,name='editar_huesped'),
    path('update/huesped/<int:id>',views.update_huesped,name='update_huesped'),
    path('eliminar/habitacion/<int:id>',views.eliminarHabitacion,name='eliminar_habitacion'),
    path('editar/habitacion/<int:id>',views.editarHabitacion,name='editar_habitacion'),
    path('update/habitacion/<int:id>',views.update_habitacion,name='update_habitacion'),
]