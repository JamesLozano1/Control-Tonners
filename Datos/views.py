from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Area, Persona, Tonner, Retiro_Tonner, Tabla_T_Toners
from .forms import FormArea, FormPersona, FormTonner, FormsRetiroTonner,FormsTabla_Toners
import base64
from django.core.files.base import ContentFile

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
        form = FormPersona(request.POST, request.FILES)  # Inicializar el formulario con datos de la solicitud POST
        if form.is_valid():  # Verificar si el formulario es válido
            firma_data = request.POST.get('firma_imagen')  # Obtener los datos de la firma en base64
            persona = form.save(commit=False)  # Guardar el formulario sin confirmar la instancia de Persona
            if firma_data:
                format, imgstr = firma_data.split(';base64,')  # Separar los datos base64
                ext = format.split('/')[-1]  # Obtener la extensión del archivo
                # Guardar la imagen de la firma en el campo 'firma' del modelo Persona
                persona.firma.save(f'firma_{persona.nombre}.{ext}', ContentFile(base64.b64decode(imgstr)), save=False)
                persona.save()  # Guardar la instancia completa de Persona con la firma
    else:
        form = FormPersona()  # Inicializar el formulario para una solicitud GET

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

def Tonners(request):
    tonners = Tonner.objects.all()

    return render(request, 'vista/tonners.html', {
        "tonner":tonners,
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