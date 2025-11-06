from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu

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