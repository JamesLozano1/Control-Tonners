from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Area, Persona, Tonner, Retiro_Tonner, Tabla_T_Toners, Tabla_T_Toners_Municipios
from .forms import FormArea, FormPersona, FormTonner, FormsRetiroTonner,FormsTabla_Toners, FormsTabla_Toners_Municipios
import base64
from django.core.files.base import ContentFile
from collections import Counter


def Inicio(request):
    title = 'BIENVENIDO'
    return render(request, 'inicio.html', {
        'title':title,
    })


def Area_U(request):

    if request.method == 'POST':
        form = FormArea(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = FormArea()
    return render(request, 'registro/R_Area.html',{
        'form': form,
    })

def Persona_U(request):
    if request.method == 'POST':
        form = FormPersona(request.POST, request.FILES)  
        if form.is_valid():  
            firma_data = request.POST.get('firma_imagen') 
            persona = form.save(commit=False) 
            if firma_data:
                format, imgstr = firma_data.split(';base64,')  
                ext = format.split('/')[-1]  
                
                persona.firma.save(f'firma_{persona.nombre}.{ext}', ContentFile(base64.b64decode(imgstr)), save=False)
                persona.save()  
    else:
        form = FormPersona()  

    return render(request, 'registro/R_Persona.html', {
        'form': form,
    })

def Tonner_U(request):

    if request.method == 'POST':
        form = FormTonner(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = FormTonner()
    return render(request, 'registro/R_Tonner.html',{
        'form': form,
    })


def Editar_Tonner(request, producto_id):
    producto = get_object_or_404(Tonner, pk=producto_id)

    if request.method == 'POST':
        form = FormTonner(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Tonners')  
    else:
        form = FormTonner(instance=producto)

    return render(request, 'vista/Editar_Tonner.html', {
        'form': form
    })

def RetiroTonner(request, producto_id):
    producto = get_object_or_404(Tonner, pk=producto_id)

    if request.method == 'POST':
        form = FormsRetiroTonner(request.POST)
        if form.is_valid():
            cantidad_retirada = form.cleaned_data['cantidad_retirada']
            if cantidad_retirada <= producto.cantidad:
                producto.cantidad -= cantidad_retirada
                producto.save()

                retiro = form.save(commit=False)
                retiro.r_tonner = producto
                retiro.cantidad_disponible = producto.cantidad
                retiro.save()

                return render(request, 'vista/retiro_success.html', {'producto': producto, 'retiro': retiro})
            else:
                form.add_error('cantidad_retirada', 'La cantidad a retirar es mayor que la disponible')
    else:
        form = FormsRetiroTonner()

    return render(request, 'vista/Retirar_Tonner.html', {'form': form, 'producto': producto})


def E_Recarga(request):
    r_tonner = Tonner.objects.filter(Estado='Recargando')
    return render(request, 'vista/T_Recargando.html', {'REtonner': r_tonner})

def E_Ocupado(request):
    r_tonner = Tonner.objects.filter(Estado='En Uso')
    return render(request, 'vista/T_Ocupado.html', {'OCtonner': r_tonner})

def E_Libre(request):
    r_tonner = Tonner.objects.filter(Estado='Disponible')
    return render(request, 'vista/T_Libre.html', {'LItonner': r_tonner})


def Editar_Tonner(request, producto_id):
    producto = get_object_or_404(Tonner, pk=producto_id)
    if request.method == 'POST':
        form = FormTonner(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('L_Tonner')  
    else:
        form = FormTonner(instance=producto)
    return render(request, 'vista/editar_tonner.html', {'form': form})

def Tabla_D_Toners(request):

    if request.method == 'POST':
        form = FormTonner(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = FormTonner()
    return render(request, 'registro/R_Tonner.html',{
        'form': form,
    })


def V_Toners_R(request):
    producto = Retiro_Tonner.objects.all()

    return render(request, 'vista/T_Ocupado.html', {
        'producto':producto,
    })

def Tabla_D_Toners_Municipios(request):

    if request.method == 'POST':
        form = FormsTabla_Toners_Municipios(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Ver_Tabla_Municipios')
    else:
        form = FormsTabla_Toners_Municipios()
    return render(request, 'Tablas/añadir_municipio.html',{
        'form': form,
    })

def ver_tabla_municipios(request):
    producto = Tabla_T_Toners_Municipios.objects.all()

    return render(request, 'Tablas/tabla_municipios.html', {
        'producto':producto,
    })

def Tabla_Impresoras_OFC(request):

    if request.method == 'POST':
        form = FormsTabla_Toners(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = FormsTabla_Toners()
    return render(request, 'Tablas/añadir_oficina.html',{
        'form': form,
    })

def Ver_Tabla(request):
    tabla = Tabla_T_Toners.objects.all()
    return render(request, 'Tablas/tabla_OFP.html', {
        'tabla':tabla,
    })

def detalle_retiro_toner(request, producto_id):
    retiro_toner = get_object_or_404(Retiro_Tonner, pk=producto_id)

    return render(request, 'vista/ver_T_EnUso.html', {'retiro_toner': retiro_toner})


def Listado_Personas(request):
    producto = Persona.objects.all()
    return render(request, 'vista/lista_personas.html', {
        'producto':producto,
    })


def Editar_Persona(request, producto_id):
    producto = get_object_or_404(Persona, pk=producto_id)
    if request.method == 'POST':
        form = FormPersona(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
    else:
        form = FormPersona(instance=producto)
    return render(request, 'Edit/editar_persona.html', {'form': form})

def buscar_Persona(request):
    query = request.GET.get('q', '')  

    personas = Persona.objects.filter(nombre__icontains=query)  
    areas = Area.objects.filter(nombre__icontains=query)

    producto = list(personas) + list(areas)

    return render(request, 'vista/lista_personas.html', {'producto': producto})

def buscar_T_OFP(request):
    query = request.GET.get('q', '')  

    tabla = Tabla_T_Toners.objects.filter(oficina__icontains=query)

    return render(request, 'Tablas/tabla_OFP.html', {'tabla': tabla})

def buscar_Tabla_T_Toners_Municipios(request):
    query = request.GET.get('q', '')  

    producto = Tabla_T_Toners_Municipios.objects.filter(oficina__icontains=query)

    return render(request, 'Tablas/tabla_municipios.html', {'producto': producto})

def buscar_toners(request):
    query = request.GET.get('q')
    LItonner = Tonner.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'vista/T_Libre.html', {'LItonner': LItonner})

def editar_t_municipios(request, producto_id):
    producto = get_object_or_404(Tabla_T_Toners_Municipios, id=producto_id)

    if request.method == 'POST':
        form = FormsTabla_Toners_Municipios(request.POST, instance=producto)
        if form.is_valid():
            form.save()
    else:
        form = FormsTabla_Toners_Municipios(instance=producto)
    return render(request, 'Edit/Editar_T_Municipios.html', {'form': form,})

def Tabla_T_Toners_OFP(request, producto_id):
    producto = get_object_or_404(Tabla_T_Toners, id=producto_id)

    if request.method == 'POST':
        form = FormsTabla_Toners(request.POST, instance=producto)
        if form.is_valid():
            form.save()
    else:
        form = FormsTabla_Toners(instance=producto)
    return render(request, 'Edit/Editar_T_OFP.html', {'form': form,})



## LO COMPLICADO ⬇

def Toner_Recarga(request):
    Toner = Tonner.objects.all()
    return render(request, 'carrito/Toner_Recargar_html', {
        'toner':Toner,
    })

def add_Lista_de_Recarga(request, producto_id):
    producto = get_object_or_404(Tonner, pk=producto_id)

    # Obtiene los productos almacenados en la cookie del carrito
    carrito = request.COOKIES.get('carrito')
    if carrito:
        carrito = carrito.split(',')  # Convierte la cadena en una lista
    else:
        carrito = []

    # Agrega el producto actual al carrito
    carrito.append(str(producto_id))

    # Crea una respuesta de redirección y establece la cookie del carrito
    response = redirect('detalle_producto', producto_id=producto_id)
    response.set_cookie('carrito', ','.join(carrito))  # Convierte la lista en una cadena separada por comas

    return response

def eliminar_de_Lista_Recarga(request, producto_id):
    producto = get_object_or_404(Tonner, pk=producto_id)

    carrito = request.COOKIES.get('carrito')
    if carrito:
        carrito = carrito.split(',')
    else:
        carrito = []

    if str(producto_id) in carrito:
        carrito.remove(str(producto_id))

    response = redirect('ver_carrito')
    response.set_cookie('carrito', ','.join(carrito))

    return response

def ver_carrito(request):
    carrito = request.COOKIES.get('carrito')
    productos_en_carrito = []
    productos = Tonner.objects.all()

    if carrito:
        carrito = carrito.split(',')  # Convertir la cadena en una lista
        carrito_count = Counter(carrito)  # Contar la cantidad de cada producto en el carrito
        producto_ids = carrito_count.keys()  # Obtener los IDs de los productos en el carrito
        productos = Tonner.objects.filter(id__in=producto_ids)  # Obtener los objetos Tonner correspondientes a los IDs

        for producto in productos:
            cantidad = carrito_count[str(producto.id)]  # Obtener la cantidad del producto en el carrito
            productos_en_carrito.append({'producto': producto, 'cantidad': cantidad})

    return render(request, 'carrito.html', {'productos_en_carrito': productos_en_carrito})




## LO COMPLICADO ⬆
