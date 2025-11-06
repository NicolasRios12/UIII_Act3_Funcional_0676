from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Restaurante, name='inicio_Restaurante'),
    path('agregar-menu/', views.agregar_Menu, name='agregar_Menu'),
    path('ver-menu/', views.ver_Menu, name='ver_Menu'),
    path('actualizar-menu/<int:id>/', views.actualizar_Menu, name='actualizar_Menu'),
    path('realizar-actualizacion-menu/<int:id>/', views.realizar_actualizacion_Menu, name='realizar_actualizacion_Menu'),
    path('borrar-menu/<int:id>/', views.borrar_Menu, name='borrar_Menu'),
]