from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu,Pedido, Reservacion

def inicio_Restaurante(request):
    return render(request, 'inicio.html')

def agregar_Menu(request):
    if request.method == 'POST':
        imagen = request.FILES.get('imagen')

        Menu.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            categoria=request.POST['categoria'],
            disponible=request.POST.get('disponible', False),
            imagen=imagen
        )
        return redirect('ver_Menu')
    return render(request, 'Menu/agregar_Menu.html')

def ver_Menu(request):
    menus = Menu.objects.all()
    return render(request, 'Menu/ver_Menu.html', {'menus': menus})

def actualizar_Menu(request, id):
    menu = get_object_or_404(Menu, id=id)
    return render(request, 'Menu/actualizar_Menu.html', {'menu': menu})

def realizar_actualizacion_Menu(request, id):
    if request.method == 'POST':
        menu = get_object_or_404(Menu, id=id)
        menu.nombre = request.POST['nombre']
        menu.descripcion = request.POST['descripcion']
        menu.precio = request.POST['precio']
        menu.categoria = request.POST['categoria']
        menu.disponible = request.POST.get('disponible', False)
        nueva_imagen = request.FILES.get('imagen')
        if nueva_imagen:
            menu.imagen = nueva_imagen
        menu.save()
        return redirect('ver_Menu')
    return redirect('ver_Menu')

def borrar_Menu(request, id):
    menu = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        menu.delete()
        return redirect('ver_Menu')
    return render(request, 'Menu/borrar_Menu.html', {'menu': menu})

# ==========================================
# VISTAS PARA PEDIDOS
# ==========================================

def agregar_pedido(request):
    if request.method == 'POST':
        try:
            menu_id = request.POST['menu']
            menu = Menu.objects.get(id=menu_id)
            cantidad = int(request.POST['cantidad'])
            total = float(menu.precio) * cantidad
            
            Pedido.objects.create(
                menu=menu,
                nombre_cliente=request.POST['nombre_cliente'],
                cantidad=cantidad,
                total=total,
                metodo_pago=request.POST['metodo_pago'],
                entregado=request.POST.get('entregado', False)
            )
            return redirect('ver_pedido')
        except Exception as e:
            # Manejar error
            return render(request, 'pedido/agregar_pedido.html', {
                'menus': Menu.objects.all(),
                'error': f"Error al crear pedido: {str(e)}"
            })
    
    menus = Menu.objects.all()
    return render(request, 'pedido/agregar_pedido.html', {'menus': menus})

def ver_pedido(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})

def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    menus = Menu.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {
        'pedido': pedido,
        'menus': menus
    })

def realizar_actualizacion_pedido(request, id):
    if request.method == 'POST':
        try:
            pedido = get_object_or_404(Pedido, id=id)
            menu_id = request.POST['menu']
            menu = Menu.objects.get(id=menu_id)
            cantidad = int(request.POST['cantidad'])
            total = float(menu.precio) * cantidad
            
            pedido.menu = menu
            pedido.nombre_cliente = request.POST['nombre_cliente']
            pedido.cantidad = cantidad
            pedido.total = total
            pedido.metodo_pago = request.POST['metodo_pago']
            pedido.entregado = request.POST.get('entregado', False)
            pedido.save()
            
            return redirect('ver_pedido')
        except Exception as e:
            # Manejar error
            pedido = get_object_or_404(Pedido, id=id)
            menus = Menu.objects.all()
            return render(request, 'pedido/actualizar_pedido.html', {
                'pedido': pedido,
                'menus': menus,
                'error': f"Error al actualizar pedido: {str(e)}"
            })
    
    return redirect('ver_pedido')

def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})