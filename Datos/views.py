from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Area, Persona, Tonner, Retiro_Tonner
from .forms import FormArea, FormPersona, FormTonner, FormsRetiroTonner


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
            form.save()

    else:
        form = FormPersona()
    return render(request, 'registro/R_Persona.html',{
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
    r_tonner = Tonner.objects.filter(Estado='R')
    return render(request, 'vista/T_Recargando.html', {'REtonner': r_tonner})

def E_Ocupado(request):
    r_tonner = Tonner.objects.filter(Estado='O')
    return render(request, 'vista/T_Ocupado.html', {'OCtonner': r_tonner})

def E_Libre(request):
    r_tonner = Tonner.objects.filter(Estado='L')
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