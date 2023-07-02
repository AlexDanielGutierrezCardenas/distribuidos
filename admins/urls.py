from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('huesped',views.huesped,name='huespedes_index'),
    path('habitacion',views.habitacion,name='habitaciones_index'),
    path('nuevo/habitacion',views.nuevo_habitacion,name='nuevo_habitacion'),
    path('nuevo/huesped',views.nuevo_huesped,name='nuevo_huesped')
]