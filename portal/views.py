from django.shortcuts import render
from django.utils import timezone
from .models import Articulo

# Create your views here.

def home(request):
    articulos_home = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')[:3]
    return render(request, "portal/index.html", {
        'articulos': articulos_home
    })