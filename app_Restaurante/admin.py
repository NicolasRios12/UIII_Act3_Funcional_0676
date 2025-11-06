from django.contrib import admin
from .models import Menu, Pedido, Reservacion

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'disponible', 'fecha_creacion']
    list_filter = ['categoria', 'disponible']
    search_fields = ['nombre', 'descripcion']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_cliente', 'menu', 'cantidad', 'total', 'entregado']
    list_filter = ['entregado', 'metodo_pago', 'fecha_pedido']

@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'correo', 'fecha_reservacion', 'hora', 'numero_personas']
    list_filter = ['fecha_reservacion'] 