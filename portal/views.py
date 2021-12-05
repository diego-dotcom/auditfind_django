from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Articulo, Seccion, User, Autor
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
    autor = Autor.objects.get(usuario=articulo.autor)

    return render(request, "portal/articulo.html", {
        "articulo": articulo,
        "articulos_aside": articulos_aside,
        "autor" : autor,
    })


def nosotros(request):
    return render(request, "portal/nosotros.html", {})


def contacto(request):

    form = FormContacto(request.POST)   

    if request.method == "POST":

        if form.is_valid():
            nombre=request.POST["nombre"]
            mail=request.POST["email"]
            consulta=request.POST["consulta"]

            mensaje = f"Usuario: \n{nombre} \n\nCorreo electrónico: \n{mail} \n\nMensaje: \n{consulta}"

            email_from = settings.EMAIL_HOST_USER
            recipient_list = settings.EMAIL_HOST_USER


            send_mail("Consulta desde la web", mensaje, email_from, [recipient_list], fail_silently=False,)
            messages.success(request, f'Mensaje enviado con éxito')

            return redirect('portal:home')  

    else:

        return render(request, "portal/contacto.html", {'form':form})        

        


@login_required
def articulo_nuevo(request):
    try:
        user = User.objects.get(username=request.user)
        if request.method == "POST":
            form = FormArticulo(request.POST, request.FILES)      
            if form.is_valid():
                articulo = form.save(commit=False)
                articulo.autor = request.user
                articulo.save()
                messages.success(request, f'Artículo publicado con éxito')
                return redirect('portal:home')          
        else:
            form = FormArticulo(initial={'fecha_publicacion':timezone.now()})
            autor = get_object_or_404(Autor, usuario_id=user.id)
            return render(request, "portal/articulo_nuevo.html", {
            "form": form,
            "autor": autor,
        })
    except:
        messages.error(request, f'No existe autor, contacte con el Administrador')
        return redirect('portal:home') 


@login_required
def articulo_editar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == "POST":  
        # user = User.objects.get(username=request.user)   
        # un_articulo.editor = user
        form = FormArticulo(data=request.POST, files=request.FILES, instance=un_articulo)
        if form.is_valid():
            form.save()
            messages.success(request, f'Articulo modificado con éxito')
            return redirect("portal:home")
    else:
        form = FormArticulo(instance = un_articulo)
        return render(request, 'portal/articulo_editar.html', {
            "articulo": un_articulo,
            "form": form
        })


@login_required
def articulo_eliminar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    un_articulo.delete()
    messages.success(request, f'Articulo eliminado con éxito')
    return redirect("portal:home")


@login_required
def autor_editar(request):
    try:
        user = User.objects.get(username=request.user)
        autor = get_object_or_404(Autor, usuario_id=user.id)
        if request.method == "POST":
            form = FormAutor(data=request.POST, files=request.FILES, instance=autor)
            if form.is_valid():
                autor = form.save(commit=False)
                autor.usuario = request.user
                autor.save()
                messages.success(request, f'Autor editado con éxito')
                return redirect('portal:home')  
        else:
            form = FormAutor(instance = autor)
            return render(request, 'portal/autor_editar.html', {
            "autor": autor,
            "form": form,
        })
    except:
        messages.error(request, f'No existe autor, contacte con el Administrador')
        return redirect('portal:home')  


def filtro_secciones(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Articulo.objects.all()
    queryset = queryset.filter(seccion=seccion).order_by('-fecha_publicacion')
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
    ).order_by('-fecha_publicacion')
    return render(request,"portal/busqueda.html", {
        "lista_articulos": lista,
        "texto": texto,
    })