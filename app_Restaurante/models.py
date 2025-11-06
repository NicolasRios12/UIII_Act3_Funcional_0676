from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='img_clientes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='pedidos')
    nombre_cliente = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre_cliente}"

class Reservacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_reservacion = models.DateField()
    hora = models.TimeField()
    numero_personas = models.PositiveIntegerField()
    menus = models.ManyToManyField(Menu, related_name='reservaciones')
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservación de {self.nombre_cliente} ({self.fecha_reservacion})"