from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Articulo, Seccion, User
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    articulos_aside = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')[:3]
    return render(request, "portal/index.html", {
        'articulos': articulos_aside,
    })

def articulos(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, "portal/articulos.html", {
        'articulos': articulos,
    })

def articulo(request, articulo_id):
    articulos_aside = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')[:3]
    articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, "portal/articulo.html", {
        "articulo": articulo,
        "articulos_aside": articulos_aside,
    })

@login_required
def articulo_nuevo(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormArticulo(request.POST, request.FILES)      
        if form.is_valid():
            form.save()
            messages.success(request, f'Artículo publicado con éxito')
            return redirect("portal:home")          
    else:
        form = FormArticulo(initial={'fecha_publicacion':timezone.now()})
        return render(request, "portal/articulo_nuevo.html", {
            "form": form,
        })

def filtro_secciones(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Articulo.objects.all()
    queryset = queryset.filter(seccion=seccion)
    return render(request,"portal/busqueda_seccion.html", {
        "lista_articulos": queryset,
        "seccion": seccion,
    })

def busqueda(request):
    texto = request.POST.get('texto', '')
    queryset = Articulo.objects.all()
    lista = queryset.filter(
        Q(titulo__contains=texto) |
        Q(copete__contains=texto)
    )
    return render(request,"portal/busqueda.html", {
        "lista_articulos": lista,
        "texto": texto,
    })