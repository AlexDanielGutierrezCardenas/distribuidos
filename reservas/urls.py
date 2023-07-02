from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('reserva_index',views.index,name='reserva_index'),
    path('reserva_nueva',views.nueva_reserva,name='nueva_reserva'),
]